# -*- coding: utf-8 -*-
{
    'name': "Invoice For Multiple Sale Order",

    'summary': """
        Helps to manage multiple sale orders in single invoice """,

    'description': """
        helps to manage multiple sale orders
    """,

    'author': "Minions 6",

    'version': '15.0.1.0',
    'depends': ['base', 'account', 'sale_management'],

    'data': [
        'views/account_move_inherit_views.xml',
    ],
}
