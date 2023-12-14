{
    'name': "Data Collection",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base','logic_base', 'mail'],
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        # 'security/record_rules.xml',
        # 'views/exam_details.xml',
        # 'views/exam_result.xml',
        'views/staff_forms.xml',
        'views/staff_web_form.xml',
    ],
    'demo': [],
    'summary': "Logic Data Collection",
    'description': "",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}