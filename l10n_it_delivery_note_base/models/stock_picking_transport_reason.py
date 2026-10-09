from odoo import fields, models

class StockPickingTransportReason(models.Model):
    _name = 'stock.picking.transport.reason'
    _description = 'Reason of Transport'
    _order = 'sequence, name, id'
    active = fields.Boolean(default=True)
    sequence = fields.Integer(index=True, default=10)
    name = fields.Char(string='Reason name', index=True, required=True, translate=True)
    note = fields.Html(string='Internal note')
