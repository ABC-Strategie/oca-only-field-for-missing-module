from odoo import fields, models

class SdiChannel(models.Model):
    _inherit = 'sdi.channel'
    channel_type = fields.Selection(selection_add=[('pec', 'PEC')], ondelete={'pec': 'cascade'})
    pec_server_id = fields.Many2one('ir.mail_server', string='Outgoing PEC server', required=False, domain=[('is_fatturapa_pec', '=', True)])
    fetch_pec_server_id = fields.Many2one('fetchmail.server', string='Incoming PEC server', required=False, domain=[('is_fatturapa_pec', '=', True)])
    email_exchange_system = fields.Char('Exchange System Email Address', help='The first time you send a PEC to SDI, you must use the address sdi01@pec.fatturapa.it.\nOdoo will automatically set this address the first time you send an e-invoice to SdI using this channel.\nThe system, with the first response or notification, communicates the PEC address to be used for future messages')
    first_invoice_sent = fields.Boolean('SDI already assigned a PEC address to my company', help='This is set after having sent the first e-invoice to SDI')
