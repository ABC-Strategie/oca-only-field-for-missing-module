from odoo import fields, models

class StockPickingTransportMethod(models.Model):
    _name = 'stock.picking.transport.method'
    _description = 'Method of Transport'
    _order = 'sequence, name, id'
    active = fields.Boolean(default=True)
    sequence = fields.Integer(index=True, default=10)
    name = fields.Char(string='Method name', index=True, required=True, translate=True)
    note = fields.Html(string='Internal note')
