from odoo import fields, models

class Project(models.Model):
    _inherit = 'project.project'
    project_status = fields.Many2one(comodel_name='project.status', copy=False, ondelete='restrict', index=True)
