from odoo import fields, models
STANDARD_ADDRESSEE_CODE = '0000000'

class ResPartner(models.Model):
    _inherit = 'res.partner'
    eori_code = fields.Char('EORI Code', size=20)
    license_number = fields.Char('License Code', size=20)
    pa_partner_code = fields.Char('PA Code for Partner', size=20)
    register = fields.Char('Professional Register', size=60)
    register_province = fields.Many2one('res.country.state')
    register_code = fields.Char('Register Registration Number', size=60)
    register_regdate = fields.Date('Register Registration Date')
    register_fiscalpos = fields.Many2one('fatturapa.fiscal_position', string='Register Fiscal Position')
    codice_destinatario = fields.Char('Addressee Code', help="The code, 7 characters long, assigned by ES to subjects with an accredited channel; if the addressee didn't accredit a channel to ES and invoices are received by PEC, the field must be the standard value ('').")
    pec_destinatario = fields.Char('Addressee PEC', help="PEC to which the electronic invoice will be sent. Must be filled ONLY when the information element <CodiceDestinatario> is '%s'" % STANDARD_ADDRESSEE_CODE)
    electronic_invoice_subjected = fields.Boolean('Enable electronic invoicing')
    electronic_invoice_obliged_subject = fields.Boolean('Obliged Subject')
    electronic_invoice_no_contact_update = fields.Boolean('Do not update the contact from Electronic Invoice Details')
    electronic_invoice_use_this_address = fields.Boolean('Use this e-invoicing data when invoicing to this address', help='Set this when the main company has got several Addressee Codes or PEC')
