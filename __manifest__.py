# -*- coding: utf-8 -*-
{
    'name': "Material Management",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Hery",
    'website': "http://h3ry.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/supplier_views.xml',
        'views/menu.xml',
        'data/data_supplier.xml',
        'data/data_material.xml',
    ],
}
