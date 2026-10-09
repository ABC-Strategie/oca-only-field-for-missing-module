from odoo import fields, models

class SdiChannel(models.Model):
    _name = 'sdi.channel'
    _inherit = 'mail.thread'
    _description = 'ES channel'
    name = fields.Char(required=True, translate=True)
    company_id = fields.Many2one('res.company', string='Company', required=True)
    channel_type = fields.Selection(string='ES channel type', selection=[], required=True, help='Channels (Pec, Web, Sftp) could be provided by external modules.')
