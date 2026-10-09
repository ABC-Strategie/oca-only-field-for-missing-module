from odoo import fields, models

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'
    income_type_id = fields.Many2one(comodel_name='payment.reason', string='Income Type')
