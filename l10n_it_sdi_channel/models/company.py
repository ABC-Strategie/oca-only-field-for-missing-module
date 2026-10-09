from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    sdi_channel_id = fields.Many2one('sdi.channel', string='ES channel')
    e_invoice_user_id = fields.Many2one(comodel_name='res.users', string='E-bill creator', help='This user will be used at supplier e-bill creation.')
