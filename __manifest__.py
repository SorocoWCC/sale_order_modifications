# -*- coding: utf-8 -*-
{
    'name': "San Miguel - Sale Order Modifications",

    'summary': """
        Sale Order Modifications""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Recicladora San Miguel",
    'website': "https://www.recicladorasanmiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'sale_order_modifications_report.xml',
        'views/sale_order.xml',
        'views/report_tiquete_venta.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}