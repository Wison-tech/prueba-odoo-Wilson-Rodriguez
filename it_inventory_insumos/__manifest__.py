# -*- coding: utf-8 -*-
{
    'name': "it_inventory_insumos",

    'summary': """
        Mantenimiento de equipos de computo por sede""",

    'description': """
        Modulo para tener seguimiento de insumos de mantenimiento
    """,

    'author': "Wilson Rodriguez",
    'website': "https://azoth-dev.vercel.app/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
