# -*- coding: utf-8 -*-
{
    'name': 'Employee Loan',
    'summary': '',
    'depends': ['base', 'hr'],
    'author': 'Ahmed Samir',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/record_rule.xml',
        'views/inherited_employee_view.xml',
        'views/employee_loan_view.xml',
        'report/report.xml',
        'report/report_inherite_hr_employee.xml',
        'data/ir_cron_employee_loan.xml',
    ],
    'demo': [
    ],
    'application': True,
}
