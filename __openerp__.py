# -*- coding: utf-8 -*-
{
    'name': "Sale Order Modifications",

    'summary': """
        Modificaciones para los pedidos de venta""",

    'description': """
        Modificaciones para los pedidos de venta
    """,

    'author': "Warren Castro",
    'website': "http://www.recicladorasanmiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'sale_order_modifications_report.xml',       
        'views/report_tiquete_venta.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
