# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
   'name': 'Office Automation (All-in-one setup)',
    'version': '1.0',
    'category': 'Tools',
    'description': """
    This module create a new Menu with all your personal emails, assigned tasks, meetings, projects and timesheets.
    """,
    'author': 'Elico Corp',
    'website': 'http://www.openerp.net.cn/',
    'depends': ['oa_base', 'oa_crm', 'oa_document', 'oa_hr_timesheet_sheet', 'oa_poweremail', 'oa_project', 'oa_sale'],
    'init_xml': [],
    'update_xml': [],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
