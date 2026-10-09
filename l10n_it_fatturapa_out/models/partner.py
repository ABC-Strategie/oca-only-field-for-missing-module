from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    max_invoice_in_xml = fields.Integer(string='Max Invoice # in XML', help='Maximum number of invoices to group in a single XML file.\nIf this is 0, then the number configured in the account settings is considered.')
