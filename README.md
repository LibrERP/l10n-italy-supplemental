<<<<<<< HEAD
[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy-supplemental.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy-supplemental)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy-supplemental/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy-supplemental?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy-supplemental/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy-supplemental)
=======
[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy)
>>>>>>> 827e0e92299f87b219a9d0bb6477984653f3b25d
[![Tech Doc](https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/dev/)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

<<<<<<< HEAD
Odoo Italian Supplemental Modules
=================================

Supplemental Italian modules for odoo (formerly OpenERP) 7.0

Warning! Follow modules replace Odoo/OCA standard modules for Italian localization:
- account_banking_pain_base
- account_banking_payment_export
- account_banking_sepa_credit_transfer

ASAP we will write integration modules but for now you must replace above modules if you want to use Italina Credit Transfer.
=======
Odoo Italia Modules
===================

Italian modules for odoo (formerly OpenERP) 7.0

http://www.odoo-italia.org/


Translation Status
------------------
[![Transifex Status](https://www.transifex.com/projects/p/OCA-l10n-italy-7-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-l10n-italy-7-0)
>>>>>>> 827e0e92299f87b219a9d0bb6477984653f3b25d


[![it](http://www.shs-av.com/wp-content/it_IT.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

<<<<<<< HEAD
Moduli Italiani aggiuntivi
==========================

Differenze rispetto localizzazione ufficiale Odoo/OCA:

- Basato su [piano dei conti](https://www.zeroincombenze.it/il-piano-dei-conti-2/) personalizzato  in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/l10n_it_fiscal)
- Basato su [codici IVA](http://wiki.zeroincombenze.org/it/Odoo/7.0/man/codici_IVA) personalizzati in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/l10n_it_fiscal)
- Classificazione [comuni italiani](http://www.shs-av.com/variazione-denominazione-comuni-italiani-2014/) aggiornata ai nuovi comuni
- [Modulo Spesometro](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/l10n_it_spesometro) con auto setup per ridurre i tempi di attivazione
- [account_banking_pain_base](https://github.com/zeroincombenze/l10n-italy-supplemental) sostituisce il relativo modulo [Odoo/OCA](https://github.com/OCA/bank-payment/tree/7.0/account_banking_pain_base)

- Modulo bonifici SEPA 7.0 non ancora ufficializzato in quanto per l'uso del Bonifico Sepa in Italia è provvisorimente sostitutivo del relativo modulo .

Modificheremo al più presto posssibile questi moduli per integrarli con i moduli standard ma, al momento, se volete gestire i bonifici Sepa con Odoo in Italia, dovete sostituire i moduli sopra elencati.

Le banche italiane non usano lo standard Sepa ma una variante definita del consorzio CBI.
=======
Moduli Odoo Italia
==================

Differenze rispetto localizzazione ufficiale Odoo/OCA:

- Il modulo [l10n_it_base](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_base) è sostituito dal modulo [l10n_it_bbone](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/l10n_it_bbone)
- Basato su [piano dei conti](https://www.zeroincombenze.it/il-piano-dei-conti-2/) personalizzato  in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental)
- Basato su [codici IVA](http://wiki.zeroincombenze.org/it/Odoo/7.0/man/codici_IVA) personalizzati in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental)
- Classificazione [comuni italiani](http://www.shs-av.com/variazione-denominazione-comuni-italiani-2014/) aggiornata ai nuovi comuni

Il modulo l10n_it_bbone è basato su [ricerca con CAP] (https://www.zeroincombenze.it/nuova-anagrafica-per-il-software-gestionale/);
inoltre il campo provincia è allineato ai moduli internazionali (utilizzo del campo state_id al posto del campo personalizzato province) ma per compatibilità con i moduli della Community Italiana, il modulo l10n_it_bbone agisce anche sul campo province.

Un wizard di conversione è fornito.
>>>>>>> 827e0e92299f87b219a9d0bb6477984653f3b25d


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be replicated on local server.

[//]: # (end copyright)



<<<<<<< HEAD


=======
>>>>>>> 827e0e92299f87b219a9d0bb6477984653f3b25d
[![chat with us](http://www.shs-av.com/wp-content/chat_with_us.png)](https://www.zeroincombenze.it/chi-siamo/contatti/)
