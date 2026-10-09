from odoo import fields, models

class StockClosePeriodLineInherit(models.Model):
    _inherit = 'stock.close.period.line'
    evaluation_method = fields.Selection(selection_add=[('production', 'Production')])
