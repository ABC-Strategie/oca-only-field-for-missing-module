from odoo import fields, models

class StockClosePeriod(models.Model):
    _name = 'stock.close.period'
    _description = 'Stock Close Period'
    name = fields.Char(string='Reference', readonly=True, required=True)
    line_ids = fields.One2many('stock.close.period.line', 'close_id', string='Product', copy=True, readonly=False)
    no_recompute_lines = fields.Boolean(string='Do not recompute lines')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'In Progress'), ('done', 'Validated'), ('cancel', 'Cancelled')], copy=False, index=True, readonly=True, string='Status')
    close_date = fields.Date(readonly=True, required=True, default=fields.Date.context_today, help='The date that will be used for the store the product quantity and average cost.')
    last_close_date = fields.Date()
    amount = fields.Float(string='Stock Amount Value', readonly=True, copy=False)
    work_start = fields.Datetime(readonly=True, default=fields.Datetime.now)
    work_end = fields.Datetime(readonly=True)
    force_evaluation_method = fields.Selection([('no_force', 'Compute based category setup'), ('purchase', 'Compute based purchase average cost'), ('standard', 'Compute based cost in product')], copy=False, help='Force Evaluation method will be used only for compute purchase costs.')
    last_closed_id = fields.Many2one('stock.close.period', string='Last Closed', copy=False, readonly=True)
    force_archive = fields.Boolean(default=False, help='Marks as archive the inventory move lines used during the process.')
    purchase_ok = fields.Boolean(default=False, readonly=True, help="Marks if action 'Compute Purchase' is processed.")
    company_id = fields.Many2one('res.company', string='Company')
    bypass_negative_qty = fields.Boolean(string='Bypass Negative Quantity', help='Ignore lines with negative quantity.')
