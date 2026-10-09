#  Copyright 2021 Marco Colombo (<https://github/TheMule71)
#  Copyright 2024 Simone Rubino - Aion Tech
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Guscio 19.0 (A.B.C. S.r.l., 2026): il modulo non definisce campi, resta solo
# perche' i DB migrati dal 16 lo hanno installato. Nessuna logica, nessun dato.

{
    "name": "ITA - Data competenza IVA e inversione contabile",
    "version": "19.0.0.0.1",
    "category": "Localization/Italy",
    "summary": "Use VAT Settlement Date in reverse charge.",
    "license": "AGPL-3",
    "author": "Marco Colombo, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-italy",
    "installable": True,
    "depends": [
        "account",
        "l10n_it_reverse_charge",
        "l10n_it_vat_settlement_date",
    ],
    # Sul 16 era auto_install: nel guscio no, per non installarlo dove non c'era.
    "auto_install": False,
    "data": [
        # "views/account_move_views.xml",
    ],
}
