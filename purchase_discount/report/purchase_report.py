from odoo import fields, models

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'
    discount = fields.Float(string='Discount (%)', digits='Discount', group_operator='avg')
