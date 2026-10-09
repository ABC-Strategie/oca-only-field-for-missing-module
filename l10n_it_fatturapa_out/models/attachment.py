from odoo import fields, models

class FatturaPAAttachment(models.Model):
    _inherit = 'fatturapa.attachment'
    _name = 'fatturapa.attachment.out'
    _description = 'Electronic Invoice'
    out_invoice_ids = fields.One2many('account.move', 'fatturapa_attachment_out_id', string='Out Invoices', readonly=True)
    has_pdf_invoice_print = fields.Boolean(help='True if all the invoices have a printed report attached in the XML, False otherwise.')
    invoice_partner_id = fields.Many2one('res.partner', string='Customer')
    state = fields.Selection(selection=[('ready', 'Ready to Send'), ('sent', 'Sent'), ('sender_error', 'Sender Error'), ('recipient_error', 'Not delivered'), ('rejected', 'Rejected (PA)'), ('validated', 'Delivered'), ('accepted', 'Accepted')], tracking=True)
    sending_user = fields.Many2one(comodel_name='res.users', readonly=True)
    sending_date = fields.Datetime('Sent Date', readonly=True)
    delivered_date = fields.Datetime(readonly=True)

class FatturaAttachments(models.Model):
    _inherit = 'fatturapa.attachments'
    is_pdf_invoice_print = fields.Boolean(help='This attachment contains the PDF report of the linked invoice')
