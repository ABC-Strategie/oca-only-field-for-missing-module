from odoo import fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    vsc_exclude_operation = fields.Boolean(
        string="Exclude from active / passive operations"
    )

    vsc_exclude_vat = fields.Boolean(string="Exclude from VAT payable / deducted")

class AccountMove(models.Model):
    _inherit = "account.move"
    
    date_vat_settlement = fields.Date(string="Date vat settlement")
