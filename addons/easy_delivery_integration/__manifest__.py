# -*- encoding: utf-8 -*-

{
    'name': 'Easy Delivery Integration',
    'version': '1.0',
    'category': 'Inventory/Delivery',
    'depends': ['delivery', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_carrier_views.xml',
        'views/stock_picking_views.xml',
    ],
    "application": True,
    'installable': True,
}