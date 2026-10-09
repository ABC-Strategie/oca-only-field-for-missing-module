from odoo import fields, models

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    main_bank_transfer_account = fields.Boolean()
    is_company_bank = fields.Boolean(default=False, store=True)
