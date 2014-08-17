{
    'name': 'Runbot Pre Build',
    'category': 'Website',
    'summary': 'Runbot',
    'version': '1.1',
    'description': "Runbot with posibility to make pre-build",
    'author': 'Vauxoo',
    'depends': ['runbot', 'runbot_language', 'runbot_pylint'],
    'data': [
        'security/runbot_team_security.xml',
        'security/ir.model.access.csv',
        'runbot_prebuild_view.xml',
    ],
    'installable': True,
}
