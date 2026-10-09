from odoo import fields, models

class AccountVatPeriodEndStatement(models.Model):
    _name = 'account.vat.period.end.statement'
    _description = 'VAT period end statement'
    _rec_name = 'date'
    _order = 'date DESC, id DESC'
    debit_vat_account_line_ids = fields.One2many('statement.debit.account.line', 'statement_id', 'Debit VAT', help='The accounts containing the debit VAT amount to write-off', readonly=True)
    credit_vat_account_line_ids = fields.One2many('statement.credit.account.line', 'statement_id', 'Credit VAT', help='The accounts containing the credit VAT amount to write-off', readonly=True)
    previous_credit_vat_account_id = fields.Many2one('account.account', 'Previous Credits VAT', help='Credit VAT from previous periods')
    previous_credit_vat_amount = fields.Float('Previous Credits VAT Amount', digits='Account')
    previous_year_credit = fields.Boolean('Previous year credits')
    previous_debit_vat_account_id = fields.Many2one('account.account', 'Previous Debits VAT', help='Debit VAT from previous periods')
    previous_debit_vat_amount = fields.Float('Previous Debits VAT Amount', digits='Account')
    interests_debit_vat_account_id = fields.Many2one('account.account', 'Due interests', help='Due interests for three-monthly statments')
    interests_debit_vat_amount = fields.Float('Due interests Amount', digits='Account')
    tax_credit_account_id = fields.Many2one('account.account', 'Tax credits')
    tax_credit_amount = fields.Float('Tax credits Amount', digits='Account')
    advance_account_id = fields.Many2one('account.account', 'Down payment')
    advance_amount = fields.Float('Down payment Amount', digits='Account')
    advance_computation_method = fields.Selection([('1', 'Storico'), ('2', 'Previsionale'), ('3', 'Analitico - effettivo'), ('4', '"4" (soggetti particolari)')], string='Down payment computation method')
    generic_vat_account_line_ids = fields.One2many('statement.generic.account.line', 'statement_id', 'Other VAT Credits / Debits or Tax Compensations')
    authority_partner_id = fields.Many2one('res.partner', 'Tax Authority Partner')
    authority_vat_account_id = fields.Many2one('account.account', 'Tax Authority VAT Account')
    journal_id = fields.Many2one('account.journal', 'Journal', required=True)
    date = fields.Date(required=True, default=fields.Date.context_today)
    move_id = fields.Many2one('account.move', 'VAT statement move', readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('paid', 'Paid')], readonly=True)
    payment_term_id = fields.Many2one('account.payment.term', 'Payment Term')
    reconciled = fields.Boolean('Paid/Reconciled', help='It indicates that the statement has been paid and the journal entry of the statement has been reconciled with one or several journal entries of payment.', readonly=True)
    residual = fields.Float(string='Amount Due', help='Remaining amount due.', digits='Account')
    payment_ids = fields.Many2many('account.move.line', string='Payments')
    date_range_ids = fields.One2many('date.range', 'vat_statement_id', 'Periods')
    interest = fields.Boolean('Compute Interest')
    interest_percent = fields.Float('Interest - Percent')
    fiscal_page_base = fields.Integer('Last printed page', required=True, default=0)
    fiscal_year = fields.Char('Fiscal year for report')
    company_id = fields.Many2one('res.company', 'Company')
    annual = fields.Boolean('Annual prospect')
    account_ids = fields.Many2many('account.account', string='Accounts filter')

class StatementDebitAccountLine(models.Model):
    _name = 'statement.debit.account.line'
    _description = 'VAT Statement debit account line'
    account_id = fields.Many2one('account.account', 'Account', required=True)
    tax_id = fields.Many2one('account.tax', 'Tax', required=True)
    statement_id = fields.Many2one('account.vat.period.end.statement', 'VAT statement')
    amount = fields.Float(required=True, digits='Account')

class StatementCreditAccountLine(models.Model):
    _name = 'statement.credit.account.line'
    _description = 'VAT Statement credit account line'
    account_id = fields.Many2one('account.account', 'Account', required=True)
    tax_id = fields.Many2one('account.tax', 'Tax', required=True)
    statement_id = fields.Many2one('account.vat.period.end.statement', 'VAT statement')
    amount = fields.Float(required=True, digits='Account')

class StatementGenericAccountLine(models.Model):
    _name = 'statement.generic.account.line'
    _description = 'VAT Statement generic account line'
    account_id = fields.Many2one('account.account', 'Account', required=True)
    statement_id = fields.Many2one('account.vat.period.end.statement', 'VAT statement')
    amount = fields.Float(required=True, digits='Account')
    name = fields.Char('Description')

class AccountTax(models.Model):
    _inherit = 'account.tax'
    vat_statement_account_id = fields.Many2one('account.account', 'Account used for VAT statement', help='The tax balance will be associated to this account after selecting the period in VAT statement')

class DateRange(models.Model):
    _inherit = 'date.range'
    vat_statement_id = fields.Many2one('account.vat.period.end.statement', 'VAT statement')
