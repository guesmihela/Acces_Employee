
{
    'name': 'Employees List Access',
    'summary': ' pour accéder à la liste des employés,il faut que administrateur vous donne accés',
    'author': 'TNT',
    'application': True,
    "sequence" : 4,
    'website': 'http://www.tnt.com.tn',
    'category': 'Human Resources',
    'version': '10.0.1.0.0',
    'depends': [
        'hr'
    ],
    'data': [
        'views/hr_employee.xml',
        'security/hr.xml',
    ],
    'installable': True,
}
