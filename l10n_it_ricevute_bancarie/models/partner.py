from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    group_riba = fields.Boolean('Group C/O', help='Group C/O by customer while issuing.')
