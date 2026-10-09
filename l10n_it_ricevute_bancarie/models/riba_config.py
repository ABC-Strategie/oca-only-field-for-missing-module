from odoo import fields, models

class RibaConfiguration(models.Model):
    _name = 'riba.configuration'
    _description = 'Configuration parameters for Cash Orders'
    _check_company_auto = True
    name = fields.Char('Description', size=64, required=True)
    type = fields.Selection([('sbf', 'Subject To Collection'), ('incasso', 'After Collection')], 'Issue Mode', required=True)
    bank_id = fields.Many2one('res.partner.bank', 'Bank Account', required=True, check_company=True, help='Bank account used for C/O issuing.')
    acceptance_journal_id = fields.Many2one('account.journal', 'Acceptance Journal', check_company=True, domain="[('company_id', '=', company_id), ('type', '=', 'bank')]", help='Journal used when C/O is accepted by the bank.')
    acceptance_account_id = fields.Many2one('account.account', 'Acceptance Account', check_company=True, help='Account used when C/O is accepted by the bank.')
    company_id = fields.Many2one('res.company', 'Company', required=True)
    accreditation_journal_id = fields.Many2one('account.journal', 'Credit Journal', check_company=True, domain="[('company_id', '=', company_id), ('type', '=', 'bank')]", help='Journal used when C/O amount is credited by the bank.')
    accreditation_account_id = fields.Many2one('account.account', 'C/O Account', check_company=True, help='Account used when C/O amount is credited by the bank.', domain="[('company_id', '=', company_id), ('internal_type', '!=', 'liquidity')]")
    bank_account_id = fields.Many2one('account.account', 'A/C Bank Account', check_company=True, domain="[('company_id', '=', company_id), ('internal_type', '=', 'liquidity')]")
    bank_expense_account_id = fields.Many2one('account.account', 'Bank Fees Account')
    unsolved_journal_id = fields.Many2one('account.journal', 'Past Due Journal', check_company=True, domain="[('company_id', '=', company_id), ('type', '=', 'bank')]", help='Journal used when C/O is past due.')
    overdue_effects_account_id = fields.Many2one('account.account', 'Past Due Bills Account', check_company=True, domain="[('company_id', '=', company_id), ('internal_type', '=', 'receivable')]")
    protest_charge_account_id = fields.Many2one('account.account', 'Protest Fee Account', check_company=True)
    settlement_journal_id = fields.Many2one('account.journal', 'Settlement Journal', check_company=True, help='Journal used when customers finally pay the invoice to bank.')
