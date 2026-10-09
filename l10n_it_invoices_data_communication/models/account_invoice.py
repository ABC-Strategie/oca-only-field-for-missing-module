from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'
    comunicazione_dati_iva_escludi = fields.Boolean(string='Exclude from invoices communication')
