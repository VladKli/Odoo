# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'wizard/wizard_view.xml',
        'views/course_and_session_views.xml',
        'views/res_partner_view.xml',
        # 'views/templates.xml',
        'data/course_data.xml',
        'data/res_partner_category_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/session_report.xml',
        'views/dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
