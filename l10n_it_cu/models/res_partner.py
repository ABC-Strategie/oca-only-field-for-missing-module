from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    income_type_id = fields.Many2one(comodel_name='payment.reason', string='Income Type')
