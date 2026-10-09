from odoo import fields, models
PRICES_TO_SHOW = [('unit', 'Unit price'), ('total', 'Total price'), ('none', 'None')]
DOMAIN_PRICES_TO_SHOW = [p[0] for p in PRICES_TO_SHOW]

class StockPickingTransportCondition(models.Model):
    _name = 'stock.picking.transport.condition'
    _description = 'Condition of Transport'
    _order = 'sequence, name, id'
    active = fields.Boolean(default=True)
    sequence = fields.Integer(index=True, default=10)
    name = fields.Char(string='Condition name', index=True, required=True, translate=True)
    price_to_show = fields.Selection(PRICES_TO_SHOW, string='Price to show', required=True, default=DOMAIN_PRICES_TO_SHOW[0])
    note = fields.Html(string='Internal note')
