# -*- coding: utf-8 -*-
{
    'name': 'SUNT Pulse',
    'version': '12.0.1.0',
    'category': 'Point of Sale',
    'website': 'https://www.hanndao.com',
    "author": "Sunt-Projects Hanndao, CoCo Yu ",
    "support": "xinrui_yu@hanndao.com",
    "license": "Other OSI approved licence",  # MIT
    'currency': 'AUD',
    'summary': "Screen for kitchen Project Pos polling.",
    'description': "POS kitchen Screen is polling order information",
    'author': "Hanndao",
    'depends': ['point_of_sale','bus'],
    'external_dependencies': {'python': [], 'bin': []},
    'data': [
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb': ['static/src/xml/pulse.xml'],
    'images': ['static/description/icon.png'],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}