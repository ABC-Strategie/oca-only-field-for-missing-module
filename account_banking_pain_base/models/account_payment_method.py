from odoo import fields, models

class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'
    pain_version = fields.Selection([], string='PAIN Version')
    convert_to_ascii = fields.Boolean(string='Convert to ASCII', default=True, help='If active, Odoo will convert each accented character to the corresponding unaccented character, so that only ASCII characters are used in the generated PAIN file.')
    warn_not_sepa = fields.Boolean(string='Warn If Not SEPA')
