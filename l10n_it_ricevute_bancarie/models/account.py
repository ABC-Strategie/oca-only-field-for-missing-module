from odoo import fields, models

class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'
    riba = fields.Boolean('C/O', default=False)
    riba_payment_cost = fields.Float('C/O Collection Fees', digits='Account', help='Collection fees amount. If different from 0, for each payment deadline an invoice line will be added to invoice, with this amount.')

class ResBankAddField(models.Model):
    _inherit = 'res.bank'
    banca_estera = fields.Boolean('Foreign Bank')

class ResPartnerBankAdd(models.Model):
    _inherit = 'res.partner.bank'
    codice_sia = fields.Char('SIA Code', size=5, help='Identification Code of the Company in the Interbank System.')

class AccountMove(models.Model):
    _inherit = 'account.move'
    riba_accredited_ids = fields.One2many('riba.distinta', 'accreditation_move_id', 'Credited C/O Slips', readonly=True)
    riba_unsolved_ids = fields.One2many('riba.distinta.line', 'unsolved_move_id', 'Past Due C/O Slips', readonly=True)
    unsolved_move_line_ids = fields.Many2many('account.move.line', 'invoice_unsolved_line_rel', 'move_id', 'line_id', 'Past Due Journal Items')
    is_unsolved = fields.Boolean('Is a past due invoice')
    riba_partner_bank_id = fields.Many2one('res.partner.bank', string='C/O Bank Account', help='Bank Account Number to which the C/O will be debited. If not set, first bank in partner will be used.', readonly=True, states={'draft': [('readonly', False)]})

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    distinta_line_ids = fields.One2many('riba.distinta.move.line', 'move_line_id', 'C/O Detail')
    unsolved_invoice_ids = fields.Many2many('account.move', 'invoice_unsolved_line_rel', 'line_id', 'move_id', 'Past Due Invoices')
    due_cost_line = fields.Boolean('C/O Collection Fees Line')
