# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '17.0.1.0.0',
    'summary': 'School management version 1.0',
    'description': """
    App quản lý trường học hehehe
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/school_information_views.xml',
        'views/class_information_views.xml',
        'views/student_information_views.xml',
        'views/subject_information_views.xml',
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
}
