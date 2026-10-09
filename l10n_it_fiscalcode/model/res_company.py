from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    fiscalcode = fields.Char(readonly=False)
