from odoo import fields, models

class StockPickingGoodsAppearance(models.Model):
    _name = 'stock.picking.goods.appearance'
    _description = 'Appearance of Goods'
    _order = 'sequence, name, id'
    active = fields.Boolean(default=True)
    sequence = fields.Integer(index=True, default=10)
    name = fields.Char(string='Appearance name', index=True, required=True, translate=True)
    note = fields.Html(string='Internal note')
