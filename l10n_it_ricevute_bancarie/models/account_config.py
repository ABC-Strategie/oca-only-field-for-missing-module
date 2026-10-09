from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    due_cost_service_id = fields.Many2one('product.product', 'Collection Fees Service')
