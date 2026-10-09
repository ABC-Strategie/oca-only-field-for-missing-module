from odoo import fields, models

class StockClosePeriodLine(models.Model):
    _name = 'stock.close.period.line'
    _description = 'Stock Close Period Line'
    _rec_name = 'product_id'
    close_id = fields.Many2one('stock.close.period', string='Stock Close Period', index=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', domain=[('type', '=', 'product')], index=True, required=True)
    product_name = fields.Char(index='trigram', translate=True)
    product_code = fields.Char(readonly=True)
    product_uom_id = fields.Many2one('uom.uom', string='UOM', required=True)
    categ_name = fields.Char(string='Category Name', readonly=True)
    evaluation_method = fields.Selection([('purchase', 'Purchase'), ('standard', 'Standard'), ('manual', 'Manual')], copy=False)
    product_qty = fields.Float(string='Quantity at Current Inventory Date', digits='Product Unit of Measure')
    price_unit = fields.Float(string='End Average Price', digits='Product Price')
    inventory_amount = fields.Float(string='Last Inventory Amount', digits='Product Price')
    inventory_qty = fields.Float(string='Last Inventory Quantity', digits='Product Unit of Measure')
    cumulative_amount = fields.Float(digits='Product Price')
    cumulative_landed_cost = fields.Float(digits='Product Price')
    cumulative_qty = fields.Float(string='Cumulative Quantity', help='Purchased quantity for evaluation purposes', digits='Product Unit of Measure')
    amount_line = fields.Float(string='Current Inventory Amount', digits='Product Price')
    location_id = fields.Many2one('stock.location', string='Location')
    lot_id = fields.Many2one('stock.lot', string='Lot/Serial Number')
    owner_id = fields.Many2one('res.partner', string='Owner')
    company_id = fields.Many2one('res.company', string='Company')
