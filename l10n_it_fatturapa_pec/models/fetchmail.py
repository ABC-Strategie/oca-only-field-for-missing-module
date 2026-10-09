from odoo import fields, models

class Fetchmail(models.Model):
    _inherit = 'fetchmail.server'
    is_fatturapa_pec = fields.Boolean('E-invoice PEC server')
    last_pec_error_message = fields.Text('Last PEC Error Message', readonly=True)
    pec_error_count = fields.Integer('PEC error count', readonly=True)
    e_inv_notify_partner_ids = fields.Many2many('res.partner', string='Contacts to notify', help="Contacts to notify when PEC message can't be processed", domain=[('email', '!=', False)])
