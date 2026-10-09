from odoo import fields, models

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    fatturapa_attachment_out_id = fields.Many2one('fatturapa.attachment.out', 'E-invoice Export File', readonly=True, copy=False)
    fatturapa_state = fields.Selection([('ready', 'Ready to Send'), ('sent', 'Sent'), ('delivered', 'Delivered'), ('accepted', 'Accepted'), ('error', 'Error')], string='E-invoice State')
