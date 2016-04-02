# -*- encoding: utf-8 -*-
##############################################################################
#
#    Acespritech Solutions Pvt. Ltd.
#    Copyright (C) 2013-2014
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
    'name': 'Point of Sale with Customer selection, Pricelist',
    'version': '1.0',
    'category': 'Point of Sale',
    'description': """
This module is used for create, select customer and pricelist associated with customer.
""",
    'author': "Acespritech Solutions Pvt. Ltd.",
    'website': "www.acespritech.com",
    'depends': ['web', 'point_of_sale', 'base'],
    'data': [],
    'demo': [],
    'test': [],
    'qweb': ['static/src/xml/pos_customer.xml'],
    'js': ['static/src/js/pos_customer.js'],
    'css': ['static/src/css/pos_customer.css'],
    'installable': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: