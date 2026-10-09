from odoo import fields, models
DELIVERY_NOTE_TYPE_CODES = [('incoming', 'Incoming'), ('outgoing', 'Outgoing'), ('internal', 'Internal')]
DOMAIN_DELIVERY_NOTE_TYPE_CODES = [s[0] for s in DELIVERY_NOTE_TYPE_CODES]

class StockDeliveryNoteType(models.Model):
    _name = 'stock.delivery.note.type'
    _description = 'Delivery Note Type'
    _order = 'sequence, name, id'
    active = fields.Boolean(default=True)
    sequence = fields.Integer(index=True, default=10)
    name = fields.Char(index=True, required=True, translate=True)
    print_prices = fields.Boolean(string='Show prices on printed DN', default=False)
    code = fields.Selection(DELIVERY_NOTE_TYPE_CODES, string='Type of Operation', required=True, default=DOMAIN_DELIVERY_NOTE_TYPE_CODES[1])
    default_transport_condition_id = fields.Many2one('stock.picking.transport.condition', string='Condition of transport')
    default_goods_appearance_id = fields.Many2one('stock.picking.goods.appearance', string='Appearance of goods')
    default_transport_reason_id = fields.Many2one('stock.picking.transport.reason', string='Reason of transport')
    default_transport_method_id = fields.Many2one('stock.picking.transport.method', string='Method of transport')
    sequence_id = fields.Many2one('ir.sequence', string='Numeration', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    note = fields.Html(string='Internal note')
