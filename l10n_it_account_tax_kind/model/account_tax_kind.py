from odoo import fields, models

class AccountTaxKind(models.Model):
    _name = 'account.tax.kind'
    _description = 'Tax exemption kind'
    _rec_names_search = ['code', 'name']
    code = fields.Char(size=4, required=True)
    name = fields.Char(required=True)
