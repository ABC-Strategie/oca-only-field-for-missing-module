# Copyright 2024 Simone Rubino - Aion Tech
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Guscio 19.0 (A.B.C. S.r.l., 2026): il modulo non definisce campi, resta solo
# perche' i DB migrati dal 16 lo hanno installato. Nessuna logica, nessun dato.

{
    "name": "ITA - Fattura elettronica - Import ZIP - Inversione contabile",
    "summary": "Importare fatture elettroniche con inversione contabile "
    "da un file ZIP.",
    "version": "19.0.0.0.1",
    "category": "Localization/Italy",
    "website": "https://github.com/OCA/l10n-italy",
    "author": "Aion Tech, Odoo Community Association (OCA)",
    "maintainers": [
        "SirAionTech",
    ],
    "license": "AGPL-3",
    "installable": True,
    # Sul 16 era auto_install: nel guscio no, per non installarlo dove non c'era.
    "auto_install": False,
    "depends": [
        "l10n_it_fatturapa_import_zip",
        "l10n_it_fatturapa_in_rc",
    ],
}
