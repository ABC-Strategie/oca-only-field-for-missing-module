# oca-only-field-for-missing-module

## A cosa serve questo repository

Questo repository **non** è una raccolta di moduli OCA pienamente funzionanti, ma uno strumento di supporto alle migrazioni Odoo (16 → 18 → 19, un branch per versione target).

## Perché esiste

Durante le migrazioni, diversi moduli OCA della localizzazione italiana (`l10n-italy`) sono stati dismessi o accorpati nelle versioni upstream più recenti e non esistono più così come erano. Se un database contiene ancora dati legati a quei moduli, la loro assenza nella versione di destinazione causa errori fatali/bloccanti durante la procedura di migrazione.

## Come funziona

Per superare il blocco, i moduli presenti in questo repository sono stati ridotti a **gusci vuoti**: mantengono solo i campi necessari (manifest e modelli minimi), senza la logica applicativa completa del modulo OCA originale. Questo è sufficiente a far sì che la migrazione proceda senza perdere i dati esistenti, che restano preservati sui campi del guscio.

## Passo successivo

Una volta completata la migrazione, in un secondo momento verranno installati i moduli OCA reali/aggiornati. Tramite script di migrazione dati, i valori verranno spostati dai campi del guscio ai nuovi campi dei moduli reali, e i moduli-guscio verranno infine dismessi.

## Nota d'uso

Questo repository va inteso come strumento transitorio legato a uno specifico intervento di migrazione, non come sostituto permanente dei moduli OCA originali.
