from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'
    variant_specific_seller_ids = fields.One2many('product.supplierinfo', 'product_id')
    po_line_ids = fields.One2many(comodel_name='purchase.order.line', inverse_name='product_id', help='Technical: used to compute quantities to purchase.')
