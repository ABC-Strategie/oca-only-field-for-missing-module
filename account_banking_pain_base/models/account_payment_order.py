from odoo import fields, models

class AccountPaymentOrder(models.Model):
    _inherit = 'account.payment.order'
    charge_bearer = fields.Selection([('SLEV', 'Following Service Level'), ('SHAR', 'Shared'), ('CRED', 'Borne by Creditor'), ('DEBT', 'Borne by Debtor')], readonly=True, tracking=True, help='Following service level : transaction charges are to be applied following the rules agreed in the service level and/or scheme (SEPA Core messages must use this). Shared : transaction charges on the debtor side are to be borne by the debtor, transaction charges on the creditor side are to be borne by the creditor. Borne by creditor : all transaction charges are to be borne by the creditor. Borne by debtor : all transaction charges are to be borne by the debtor.')
    batch_booking = fields.Boolean(readonly=True, tracking=True, help='If true, the bank statement will display only one debit line for all the wire transfers of the SEPA XML file ; if false, the bank statement will display one debit line per wire transfer of the SEPA XML file.')
