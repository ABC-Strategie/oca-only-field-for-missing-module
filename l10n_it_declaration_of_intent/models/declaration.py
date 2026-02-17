# Copyright 2017 Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class DeclarationOfIntentYearlyLimit(models.Model):
    _name = "l10n_it_declaration_of_intent.yearly_limit"
    _description = "Yearly limit for declarations"
    _order = "company_id, year desc"
    _rec_name = "year"

    company_id = fields.Many2one("res.company", string="Company")
    year = fields.Char(required=True)
    limit_amount = fields.Float()
    used_amount = fields.Float(string="Used amount")

   

class DeclarationOfIntent(models.Model):
    _name = "l10n_it_declaration_of_intent.declaration"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Declaration of intent"
    _order = "date_start desc,date_end desc"

    @api.model
    def _default_currency(self):
        return self.env.company.currency_id

    number = fields.Char(copy=False)
    date = fields.Date(required=True, string="Telematic Protocol Date")
    date_start = fields.Date(required=True)
    date_end = fields.Date(required=True)
    type = fields.Selection(
        [("in", "Issued from company"), ("out", "Received from customers")],
        required=True,
        default="in",
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    telematic_protocol = fields.Char(required=True)
    partner_document_number = fields.Char(
        string="Document Number", help="Number of partner's document"
    )
    partner_document_date = fields.Date(
        string="Document Date", help="Date of partner's document"
    )
    taxes_ids = fields.Many2many("account.tax", string="Taxes", required=True)
    used_amount = fields.Monetary(string="Used Amount", store=True)
    limit_amount = fields.Monetary(required=True)
    available_amount = fields.Monetary(string = "Available amount")
    company_id = fields.Many2one(
        "res.company", string="Company", default=lambda self: self.env.company
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        default=_default_currency,
    )
    fiscal_position_id = fields.Many2one(
        "account.fiscal.position",
        string="Fiscal Position",
        required=True,
        domain=[("valid_for_declaration_of_intent", "=", True)],
    )
    state = fields.Selection(
        [("valid", "Valid"), ("expired", "Expired"), ("close", "Close")],
        string = "State",
        store=True,
    )
    force_close = fields.Boolean()
    line_ids = fields.One2many(
        comodel_name="l10n_it_declaration_of_intent.declaration_line",
        inverse_name="declaration_id",
        string="Lines",
    )

 


class DeclarationOfIntentLine(models.Model):
    _name = "l10n_it_declaration_of_intent.declaration_line"
    _description = "Details of declaration of intent"

    declaration_id = fields.Many2one(
        comodel_name="l10n_it_declaration_of_intent.declaration",
        string="Declaration",
    )
    taxes_ids = fields.Many2many("account.tax", string="Taxes")
    move_line_ids = fields.Many2many(
        comodel_name="account.move.line",
        relation="move_line_declaration_line_rel",
        string="Move Lines",
        ondelete="cascade",
    )
    amount = fields.Monetary()
    base_amount = fields.Monetary()
    invoice_id = fields.Many2one("account.move", string="Invoice", ondelete="cascade")
    date_invoice = fields.Date(related="invoice_id.invoice_date", string="Date Invoice")
    company_id = fields.Many2one(
        "res.company", string="Company", related="declaration_id.company_id"
    )
    currency_id = fields.Many2one("res.currency", string="Currency")
