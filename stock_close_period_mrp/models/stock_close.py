from odoo import fields, models

class StockClosePeriodInherit(models.Model):
    _inherit = 'stock.close.period'
    force_standard_price = fields.Boolean(default=False, help='Forces the use of the standard price instead of calculating the cost from the BOM.')
    production_ok = fields.Boolean(default=False, readonly=True, help="Marks if action 'Compute Production' is processed.")
