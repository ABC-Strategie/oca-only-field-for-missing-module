from odoo import fields, models

class FatturaPAAttachmentImportZIP(models.Model):
    _name = 'fatturapa.attachment.import.zip'
    _description = 'E-bill ZIP import'
    _inherits = {'ir.attachment': 'ir_attachment_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin', 'l10n_it_fatturapa.attachment.e_invoice.link']
    _order = 'id desc'
    ir_attachment_id = fields.Many2one('ir.attachment', 'Attachment', required=True, ondelete='cascade')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Completed')], required=True, readonly=True)
    attachment_out_ids = fields.One2many('fatturapa.attachment.out', 'attachment_import_zip_id', string='Attachments Out', readonly=True)
    attachment_in_ids = fields.One2many('fatturapa.attachment.in', 'attachment_import_zip_id', string='Attachments In', readonly=True)
    invoice_out_ids = fields.One2many('account.move', 'attachment_out_import_zip_id', string='Invoices Out')
    invoice_in_ids = fields.One2many('account.move', 'attachment_in_import_zip_id', string='Invoices In')

class FatturaPAAttachmentIn(models.Model):
    _inherit = 'fatturapa.attachment.in'
    attachment_import_zip_id = fields.Many2one('fatturapa.attachment.import.zip', 'E-bill ZIP import', readonly=True, ondelete='restrict')

class FatturaPAAttachmentOut(models.Model):
    _inherit = 'fatturapa.attachment.out'
    attachment_import_zip_id = fields.Many2one('fatturapa.attachment.import.zip', 'E-bill ZIP import', readonly=True, ondelete='restrict')
