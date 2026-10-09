# Copyright 2024 Lorenzo Battistini
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# Guscio 19.0 (A.B.C. S.r.l., 2026): il modulo non definisce campi, resta solo
# perche' i DB migrati dal 16 lo hanno installato. Nessuna logica, nessun dato.
{
    "name": "ITA - Ritenute d'acconto - Financial Reports",
    "summary": "Integrazione Ritenute d'acconto e Rendiconti contabili",
    "version": "19.0.0.0.1",
    "development_status": "Beta",
    "category": "Hidden",
    "website": "https://github.com/OCA/l10n-italy",
    "author": "Innovyou, Odoo Community Association (OCA)",
    "maintainers": ["eLBati"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # Sul 16 era auto_install: nel guscio no, per non installarlo dove non c'era.
    "auto_install": False,
    "depends": [
        "l10n_it_withholding_tax",
        "account_financial_report",
    ],
    "data": [
        # "report/templates/open_items.xml",
    ],
}
