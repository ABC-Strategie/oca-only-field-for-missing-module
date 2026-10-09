from odoo import fields, models

class Communication(models.Model):
    _inherit = 'comunicazione.dati.iva'
    exclude_e_invoices = fields.Boolean('Exclude e-invoices', default=True)
