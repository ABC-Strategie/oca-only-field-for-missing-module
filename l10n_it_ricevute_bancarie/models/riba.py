from odoo import fields, models

class RibaList(models.Model):
    _name = 'riba.distinta'
    _description = 'C/O Slip'
    _inherit = ['mail.thread']
    _order = 'date_created desc'
    name = fields.Char('Reference', required=True, readonly=True, states={'draft': [('readonly', False)]})
    config_id = fields.Many2one('riba.configuration', string='Configuration', index=True, required=True, readonly=True, states={'draft': [('readonly', False)]}, help='C/O configuration to be used.')
    state = fields.Selection([('draft', 'Draft'), ('accepted', 'Accepted'), ('accredited', 'Credited'), ('paid', 'Paid'), ('unsolved', 'Past Due'), ('cancel', 'Canceled')], 'State', readonly=True)
    line_ids = fields.One2many('riba.distinta.line', 'distinta_id', 'C/O Due Dates', readonly=True, states={'draft': [('readonly', False)]})
    user_id = fields.Many2one('res.users', 'User', required=True, readonly=True, states={'draft': [('readonly', False)]})
    date_created = fields.Date('Creation Date', readonly=True)
    date_accepted = fields.Date('Acceptance Date')
    date_accreditation = fields.Date('Credit Date')
    date_paid = fields.Date('Payment Date', readonly=True)
    date_unsolved = fields.Date('Past Due Date', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, readonly=True, states={'draft': [('readonly', False)]})
    accreditation_move_id = fields.Many2one('account.move', 'Credit Entry', readonly=True)
    registration_date = fields.Date('Registration Date', states={'draft': [('readonly', False)], 'cancel': [('readonly', False)]}, readonly=True, required=True, help='Keep empty to use the current date.')

class RibaListLine(models.Model):
    _name = 'riba.distinta.line'
    _inherit = 'mail.thread'
    _description = 'C/O Details'
    _rec_name = 'sequence'
    sequence = fields.Integer('Number')
    move_line_ids = fields.One2many('riba.distinta.move.line', 'riba_line_id', string='Credit Move Lines')
    acceptance_move_id = fields.Many2one('account.move', string='Acceptance Entry', readonly=True)
    unsolved_move_id = fields.Many2one('account.move', string='Past Due Entry', readonly=True)
    acceptance_account_id = fields.Many2one('account.account', string='Acceptance Account')
    bank_id = fields.Many2one('res.partner.bank', string='Debtor Bank')
    distinta_id = fields.Many2one('riba.distinta', string='Slip', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    due_date = fields.Date('Due Date', readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('accredited', 'Credited'), ('paid', 'Paid'), ('unsolved', 'Past Due'), ('cancel', 'Canceled')], 'State', readonly=True, tracking=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True, related_sudo=False)

class RibaListMoveLine(models.Model):
    _name = 'riba.distinta.move.line'
    _description = 'C/O Details'
    _rec_name = 'amount'
    amount = fields.Float('Amount', digits='Account')
    move_line_id = fields.Many2one('account.move.line', string='Credit Move Line')
    riba_line_id = fields.Many2one('riba.distinta.line', string='Slip Line', ondelete='cascade')
