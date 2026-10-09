from odoo import fields, models

class FatturaPAAttachmentOut(models.Model):
    _inherit = 'fatturapa.attachment.out'
    last_sdi_response = fields.Text(string='Last Response from Exchange System', default='No response yet', readonly=True)
