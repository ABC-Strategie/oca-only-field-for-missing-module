# Copyright 2017 Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
# Copyright 2022 Michele Rusticucci <michele.rusticucci@agilebg.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.misc import format_date


class AccountMove(models.Model):
    _inherit = "account.move"

    declaration_of_intent_ids = fields.Many2many(
        comodel_name="l10n_it_declaration_of_intent.declaration",
        string="Declarations of intent",
    )

    def select_manually_declarations(self):
        return False


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    force_declaration_of_intent_id = fields.Many2one(
        comodel_name="l10n_it_declaration_of_intent.declaration",
        string="Force Declaration of Intent",
    )
