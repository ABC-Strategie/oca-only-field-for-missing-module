from odoo import fields, models

class ComunicazioneLiquidazione(models.Model):
    _inherit = ['mail.thread']
    _name = 'comunicazione.liquidazione'
    _description = 'VAT statement communication'
    company_id = fields.Many2one('res.company', string='Company', required=True)
    identificativo = fields.Integer(string='Identifier')
    year = fields.Integer(required=True)
    last_month = fields.Integer(string='Last month')
    liquidazione_del_gruppo = fields.Boolean(string="Group's statement")
    taxpayer_vat = fields.Char(string='Vat', required=True)
    controller_vat = fields.Char(string='Controller TIN')
    taxpayer_fiscalcode = fields.Char()
    declarant_different = fields.Boolean(string='Declarant different from taxpayer', default=True)
    declarant_fiscalcode = fields.Char()
    declarant_fiscalcode_company = fields.Char(string='Fiscalcode company')
    codice_carica_id = fields.Many2one('appointment.code', string='Role code')
    declarant_sign = fields.Boolean(string='Declarant sign', default=True)
    delegate_fiscalcode = fields.Char()
    delegate_commitment = fields.Selection([('1', 'Communication prepared by taxpayer'), ('2', 'Communication prepared by sender')], string='Commitment')
    delegate_sign = fields.Boolean(string='Delegate sign')
    date_commitment = fields.Date(string='Date commitment')
    quadri_vp_ids = fields.One2many('comunicazione.liquidazione.vp', 'comunicazione_id', string='VP tables')
    iva_da_versare = fields.Float(string='VAT to pay', readonly=True)
    iva_a_credito = fields.Float(string='Credit VAT', readonly=True)

class ComunicazioneLiquidazioneVp(models.Model):
    _name = 'comunicazione.liquidazione.vp'
    _description = 'VAT statement communication - VP table'
    comunicazione_id = fields.Many2one('comunicazione.liquidazione', string='Communication', readonly=True)
    period_type = fields.Selection([('month', 'Monthly'), ('quarter', 'Quarterly')], string='Period type')
    month = fields.Integer(default=False)
    quarter = fields.Integer(default=False)
    subcontracting = fields.Boolean()
    exceptional_events = fields.Selection([('1', 'Code 1'), ('9', 'Code 9')], string='Exceptional events')
    imponibile_operazioni_attive = fields.Float(string='Profitable operations total (without VAT)')
    imponibile_operazioni_passive = fields.Float(string='Unprofitable operations total (without VAT)')
    iva_esigibile = fields.Float(string='Due VAT')
    iva_detratta = fields.Float(string='Deducted VAT')
    iva_dovuta_debito = fields.Float(string='Debit VAT')
    iva_dovuta_credito = fields.Float(string='Credit due VAT')
    debito_periodo_precedente = fields.Float(string='Previous period debit')
    credito_periodo_precedente = fields.Float(string='Previous period credit')
    credito_anno_precedente = fields.Float(string='Previous year credit')
    versamento_auto_UE = fields.Float(string='Auto UE payment')
    crediti_imposta = fields.Float(string='Tax credits')
    interessi_dovuti = fields.Float(string='Due interests for quarterly statements')
    accounto_dovuto = fields.Float(string='Down payment due')
    metodo_calcolo_acconto = fields.Selection([('1', 'Storico'), ('2', 'Previsionale'), ('3', 'Analitico - effettivo'), ('4', '"4" (soggetti particolari)')], string='Down payment computation method')
    iva_da_versare = fields.Float(string='VAT to pay')
    iva_a_credito = fields.Float(string='Credit VAT')
    liquidazioni_ids = fields.Many2many('account.vat.period.end.statement', 'comunicazione_iva_liquidazioni_rel', 'comunicazione_id', 'liquidazione_id', string='VAT statements')
