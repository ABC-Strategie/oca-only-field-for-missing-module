from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    bank_transfer_account = fields.Many2one('res.partner.bank')
