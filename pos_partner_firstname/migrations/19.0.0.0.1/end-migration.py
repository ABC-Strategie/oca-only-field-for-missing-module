# Copyright 2026 A.B.C. S.r.l.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
"""Il guscio si disinstalla da solo a fine aggiornamento.

Gli script "end-" girano dopo che tutti i moduli sono stati caricati, e solo
per i moduli in aggiornamento (odoo/modules/loading.py, STEP 3.5): cioe' sui DB
che arrivano dal 16 con pos_partner_firstname installato. A quel punto il
modulo e' "installed" e si usa la routine standard di disinstallazione,
module_uninstall(): toglie i dati del solo modulo (record condivisi con altri
moduli restano) e lo mette "uninstalled". Il modulo non ha campi ne' tabelle.
"""

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

MODULE = "pos_partner_firstname"


@openupgrade.migrate()
def migrate(env, version):
    Module = env["ir.module.module"]
    module = Module.search([("name", "=", MODULE), ("state", "=", "installed")])
    if not module:
        return
    dependents = Module.search(
        [
            ("dependencies_id.name", "=", MODULE),
            ("state", "in", ("installed", "to install", "to upgrade")),
        ]
    )
    if dependents:
        _logger.warning(
            "%s non disinstallato: ne dipendono %s", MODULE, dependents.mapped("name")
        )
        return
    module.module_uninstall()
    _logger.info("%s: guscio disinstallato a fine aggiornamento", MODULE)
