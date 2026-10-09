from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    fiscalcode = fields.Char('Fiscal Code', size=16, help='Italian Fiscal Code')
