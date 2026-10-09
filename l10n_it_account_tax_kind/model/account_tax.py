from odoo import fields, models

class AccountTax(models.Model):
    _inherit = 'account.tax'
    kind_id = fields.Many2one('account.tax.kind', string='Exemption Kind')
    law_reference = fields.Char('Law reference')
