from odoo import fields, models

class ResCityItCode(models.Model):
    _name = 'res.city.it.code'
    _description = 'National city codes'
    national_code = fields.Char('National code', size=4)
    cadastre_code = fields.Char('Belfiore cadastre code (not used anymore)', size=4)
    province = fields.Char(size=5)
    name = fields.Char()
    notes = fields.Char(size=4)
    national_code_var = fields.Char('National code variation', size=4)
    cadastre_code_var = fields.Char('Cadastre code variation', size=4)
    province_var = fields.Char('Province variation', size=5)
    name_var = fields.Char('Name variation', size=100)
    creation_date = fields.Date()
    var_date = fields.Date('Variation date')

class ResCityItCodeDistinct(models.Model):
    _name = 'res.city.it.code.distinct'
    _description = 'National city codes distinct'
    _auto = False
    name = fields.Char(size=100)
