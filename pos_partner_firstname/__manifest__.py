# Copyright 2021 initOS Gmbh
# Copyright 2019 Roberto Fichera
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# Guscio 19.0 (A.B.C. S.r.l., 2026) che SI DISINSTALLA DA SOLO.
# Sulla 19 il POS modifica i clienti con il form del backend
# (point_of_sale: res_partner_action_edit_pos -> base.view_partner_form), che ha
# gia' privato/azienda e, con partner_firstname, nome e cognome. Il modulo non
# definisce campi: serve solo a portare fuori dallo stato "to upgrade" i DB
# migrati dal 16. Lo script migrations/19.0.0.0.1/end-migration.py lo
# disinstalla a fine aggiornamento.

{
    "name": "POS Partner Firstname",
    "summary": "POS Support of partner firstname",
    "version": "19.0.0.0.1",
    "development_status": "Beta",
    "category": "Point Of Sale",
    "website": "https://github.com/OCA/pos",
    "author": "Roberto Fichera, Odoo Community Association (OCA)",
    "maintainers": ["robyf70"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # Sul 16 era auto_install: nel guscio no, per non installarlo dove non c'era.
    "auto_install": False,
    "depends": [
        "point_of_sale",
        "partner_firstname",
        # "pos_partner_is_company",  <-- non esiste sulla 19, e il form nativo lo rende inutile
    ],
    "external_dependencies": {
        "python": ["openupgradelib"],
    },
    # "assets": {
    #     "point_of_sale.assets": [
    #         "pos_partner_firstname/static/src/js/PartnerDetailsEdit.js",
    #         "pos_partner_firstname/static/src/js/PartnerScreen.js",
    #         "pos_partner_firstname/static/src/xml/pos.xml",
    #     ],
    # },
}
