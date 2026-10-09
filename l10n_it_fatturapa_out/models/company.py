from odoo import fields, models
_DEFAULT_XML_DIVISA_VALUE = 'force_eur'

class ResCompany(models.Model):
    _inherit = 'res.company'
    e_invoice_transmitter_id = fields.Many2one('res.partner', 'E-bill Transmitter', help='This partner will be used as transmitter in out invoice.', required=True)
    max_invoice_in_xml = fields.Integer(string='Max Invoice # in XML', default=0, help='Customer default for maximum number of invoices to group in a single XML file. 0=Unlimited')
    xml_divisa_value = fields.Selection([('keep_orig', 'Keep original'), ('force_eur', 'Force euro')], string='XML Divisa value', default=_DEFAULT_XML_DIVISA_VALUE)
