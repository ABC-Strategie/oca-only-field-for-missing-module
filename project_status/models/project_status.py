from odoo import fields, models

class ProjectStatus(models.Model):
    _name = 'project.status'
    _order = 'status_sequence'
    _description = 'Project Status'
    name = fields.Char(required=True, translate=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company')
    description = fields.Char(translate=True)
    status_sequence = fields.Integer(string='Sequence')
    is_closed = fields.Boolean(string='Is Closed Status', help='Specify if this is a closing status.')
    fold = fields.Boolean(string='Folded')
