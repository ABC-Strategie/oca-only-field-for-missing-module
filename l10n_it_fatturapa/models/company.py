from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    fatturapa_fiscal_position_id = fields.Many2one('fatturapa.fiscal_position', 'Electronic Invoice Fiscal Position', help='Fiscal position used by electronic invoice')
    fatturapa_art73 = fields.Boolean('Art. 73')
    fatturapa_pub_administration_ref = fields.Char('Public Administration Reference Code', size=20)
    fatturapa_tax_representative = fields.Many2one('res.partner', 'Legal Tax Representative')
    fatturapa_sender_partner = fields.Many2one('res.partner', 'Third Party/Sender', help='Data of Third-Party Issuer Intermediary who emits the invoice on behalf of the seller/provider')
    fatturapa_stabile_organizzazione = fields.Many2one('res.partner', 'Stable Organization', help='The fields must be entered only when the seller/provider is non-resident, with a stable organization in Italy')
    fatturapa_preview_style = fields.Selection([('Foglio_di_stile_fatturaordinaria_v1.2.2.xsl', 'Fattura Ordinaria'), ('FoglioStileAssoSoftware.xsl', 'AssoSoftware'), ('FoglioStileSouthTyrol-bilingue.xsl', 'South-Tyrol')], string='Preview Format Style for Fattura Ordinaria', required=True, default='Foglio_di_stile_fatturaordinaria_v1.2.2.xsl')
    fatturapa_simple_preview_style = fields.Selection([('fatturasemplificata_v1.0.xsl', 'Fattura Semplificata')], string='Preview Format Style for Fattura Semplificata', required=True, default='fatturasemplificata_v1.0.xsl')
