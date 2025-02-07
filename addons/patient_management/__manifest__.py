# -*- coding: utf-8 -*-
{
    'name': "patient_management",

    'summary': """
        This module processes patients management""",

    'description': """
        This module processes patients management
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail'
    ],

    # always loaded
    'data': [
        #security
        'security/ir.model.access.csv',
        #views
        'views/patient_base_views.xml',
        #report
        'report/patient_raport.xml',
        #wizard
        'wizard/patient_wizard_views.xml'
    ],

}
