# -*- coding: utf-8 -*-
{
    'name': "Student management",

    'summary': """
       This module processes students management
    """,

    'description': """
        This module processes students management
    """,

    'author': "",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 
                'contacts'
    ],

    # always loaded
    'data': [
        'data/ir_sequence_res_partner.xml',
        'data/ir_sequence_sudent_base.xml',
        'security/ir.model.access.csv',
        'views/student_base_views.xml',
        'views/student_class_views.xml',
        'views/res_partner_views.xml',
        'views/model_wizard_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
