from odoo import fields, models

class FatturaPAAttachment(models.AbstractModel):
    _inherit = 'fatturapa.attachment'
    channel_id = fields.Many2one(comodel_name='sdi.channel')
