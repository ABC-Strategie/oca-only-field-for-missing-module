from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'
    declaration_of_intent_ids = fields.Many2many(comodel_name='l10n_it_declaration_of_intent.declaration', string='Declarations of intent')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    force_declaration_of_intent_id = fields.Many2one(comodel_name='l10n_it_declaration_of_intent.declaration', string='Force Declaration of Intent')
