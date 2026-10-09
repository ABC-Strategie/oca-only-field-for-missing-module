from odoo import fields, models

class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'
    is_fatturapa_pec = fields.Boolean('E-invoice PEC server')
    email_from_for_fatturaPA = fields.Char('Sender Email Address')
