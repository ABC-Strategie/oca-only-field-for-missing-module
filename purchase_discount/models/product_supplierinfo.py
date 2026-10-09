from odoo import fields, models

class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
    discount = fields.Float(string='Discount (%)', digits='Discount', readonly=False)
