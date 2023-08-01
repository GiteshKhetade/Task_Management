# -*- coding: utf-8 -*-
{
    'name': "school",

    'summary': """school
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'sequence' : "-100",
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/meeting_wizard.xml',
        'views/school_teacher_views.xml',
        'views/school_student_views.xml',
        'views/student_details_views.xml',
        'views/school_meeting_views.xml',
        'views/school_employeeinfo_views.xml',
        'views/school_companyinfo_views.xml',
        'views/school_course_views.xml',
        'views/school_menu_views.xml',
        'report/report.xml',
        'report/teacher_card.xml',
        'report/student_card.xml'

        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable' : True,
    'application' : True,
    'auto-install' : False

}

