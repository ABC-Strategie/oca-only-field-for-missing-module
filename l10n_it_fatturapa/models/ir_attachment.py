from odoo import fields, models

class FatturaPAAttachment(models.Model):
    _name = 'fatturapa.attachment'
    _description = 'SdI file'
    _inherits = {'ir.attachment': 'ir_attachment_id'}
    _inherit = ['mail.thread', 'l10n_it_fatturapa.attachment.e_invoice.link']
    _order = 'id desc'
    id = fields.Id()
    ir_attachment_id = fields.Many2one(comodel_name='ir.attachment', string='Attachment', required=True, ondelete='cascade')
    att_name = fields.Char(string='SdI file name')
    ftpa_preview_link = fields.Char('Preview link', readonly=True)
