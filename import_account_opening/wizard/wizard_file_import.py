# © 2021-2022 SHS-AV srl (www.shs-av.com)
# © 2022 - Didotech srl <https://www.didotech.com>

import base64
from io import BytesIO
from openpyxl import load_workbook
# from unidecode import unidecode
from odoo import models, fields, api, _
from dataclasses import dataclass
import logging
_logger = logging.getLogger(__name__)


@dataclass
class Excel:
    A: int = 0
    B: int = 1
    C: int = 2
    D: int = 3
    E: int = 4
    F: int = 5
    G: int = 6
    H: int = 7
    I: int = 8
    J: int = 9
    K: int = 10
    L: int = 11
    M: int = 12
    N: int = 13
    O: int = 14


columns = {
    'code': Excel.A,   # account code
    'name': Excel.F,
    # 'customer': Excel.N,
    # 'supplier': Excel.O,
    'debit': Excel.J,
    'credit': Excel.K,
    'ref': Excel.G,
    'date_maturity': Excel.I,
    'vat': Excel.M
}


class WizardImportAccountOpening(models.Model):
    _name = "wizard.import.account.opening"
    _description = "Import Account Opening from xlsx"

    data_file = fields.Binary(
        string='Excel Data File',
        required=True,
    )
    filename = fields.Char()
    journal_id = fields.Many2one(
        'account.journal', string='Journal', required=True
    )
    account_id = fields.Many2one(
        'account.account', string='Open account', required=True
    )
    dry_run = fields.Boolean(string='Dry-run', default=False)
    tracelog = fields.Html('Result History')

    @api.multi
    def html_txt(self, text, tag):
        if tag:
            if tag in ('table', '/table', 'tr', '/tr'):
                if not text and tag == 'table':
                    text = (
                        'border="2px" cellpadding="2px" style="padding: 5px"'
                    )
                if text:
                    html = '<%s %s>' % (tag, text)
                elif tag.startswith('/'):
                    html = '<%s>\n' % tag
                else:
                    html = '<%s>' % tag
            else:
                html = '<%s>%s</%s>' % (tag, text, tag)
        else:
            html = text
        return html

    def html_add_row(self, row):
        html = self.html_txt('', 'tr')
        for cell in row:
            html += self.html_txt(cell, 'td')
        html += self.html_txt('', '/tr')
        return html

    def get_data(self):
        contents = {}
        wb = load_workbook(BytesIO(base64.b64decode(self.data_file)))
        sheet = wb.active

        hdr = True
        for line in sheet.rows:
            if line[Excel.B].value and not line[Excel.C].value:
                partner = line[Excel.B].value.strip()
                contents[partner] = []
                hdr = True
                continue
            elif hdr:
                hdr = False
                continue
            elif not line[1].value:
                continue

            row = {}
            for key, column in columns.items():
                row[key] = line[column].value

            contents[partner].append(row)
        return contents

    def get_account_code(self, acc_domain, vals, numrec):
        recs = self.env['account.account'].search(acc_domain)

        if len(recs) != 1:
            row_values = [str(numrec), '', vals.get('name', ''), '']
            if len(recs) > 1:
                row_values.append(_('Found multiple records.'))
            else:
                row_values.append(_('No record found!'))
            html = self.html_add_row(row_values)
            account_id = False
        else:
            html = ''
            account_id = recs[0].id
        return account_id, html

    def sanitize(self, name):
        names = name.split()
        return ' '.join([n.strip() for n in names if n])

    @api.multi
    def import_xls(self):
        self.tracelog = ''
        file_datas = self.get_data()
        for partner_name, datas in file_datas.items():
            partner_name = self.sanitize(partner_name)
            partner = self.env['res.partner'].search([
                ('name', '=', partner_name),
                ('parent_id', '=', False)
            ])

            if not len(partner) == 1 and datas[0]['vat']:
                partner = self.env['res.partner'].search([
                    '|',
                    ('vat', '=', datas[0]['vat']),
                    ('fiscalcode', '=', datas[0]['vat']),
                    ('parent_id', '=', False)
                ])

            if len(partner) == 1:
                _logger.info(f'Creating accounting record record for "{partner_name}"')
                self.create_accounting_record(partner, datas)
            elif partner:
                _logger.info(f'Error: Too many partners "{partner_name}"')
            else:
                _logger.info(f'Error: No partners "{partner_name}"')

        return {
            'name': 'Import result',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.import.account.opening',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'view_id': self.env.ref(
                'import_account_opening.wizard_import_account_opening_result'
            ).id,
            'domain': [('id', '=', self.id)],
        }

    @api.multi
    def create_accounting_record(self, partner, datas):
        move_model = 'account.move'
        company_id = self.env.user.company_id.id
        move_line_model = 'account.move.line'

        if not self.dry_run:
            move = self.env[move_model].create(
                {
                    'company_id': company_id,
                    'journal_id': self.journal_id.id,
                    'move_type': 'other',
                    'type': 'entry',
                    'ref': 'apertura conti',
                }
            )

        tracelog = self.html_txt(_(f'Import account entries for {partner.name}'), 'h3')
        tracelog += self.html_txt('', 'table')
        tracelog += self.html_add_row([_('Row'), _('Code'), _('Name'), _('Vat'), _('Note')])

        total_debit = 0.0
        total_credit = 0.0

        for numrec, vals in enumerate(datas, start=1):
            vals['partner_id'] = partner.id
            del(vals['vat'])

            acc_domain = [
                ('code', '=', vals.pop('code')),
                ('company_id', '=', company_id)
            ]
            vals['account_id'], html = self.get_account_code(acc_domain, vals, numrec)
            tracelog += html

            if not vals or self.dry_run:
                continue
            else:
                vals['move_id'] = move.id
                try:
                    self.env[move_line_model].with_context(
                        check_move_validity=False
                    ).create(vals)
                    total_debit += vals.get('debit', 0.0)
                    total_credit += vals.get('credit', 0.0)
                except BaseException as e:
                    tracelog += self.html_add_row(['%s' % numrec, '', vals.get('name', ''), '', e])
                    break

        if not self.dry_run:
            vals = {
                'move_id': move.id,
                'account_id': self.account_id.id,
                'name': 'risultato di esercizio',
            }
            if total_credit > total_debit:
                vals['debit'] = total_credit - total_debit
            else:
                vals['credit'] = total_debit - total_credit

            self.env[move_line_model].create(vals)

        tracelog += self.html_txt('', '/table')
        self.tracelog += tracelog

    def close_window(self):
        return {'type': 'ir.actions.act_window_close'}
