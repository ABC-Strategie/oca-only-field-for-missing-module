from odoo import fields, models

class XlsxStockClosePeriod(models.AbstractModel):
    _name = 'report.stock_close_period.report_xlsx_stock_close_print'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Report Stock Close XLSX'
