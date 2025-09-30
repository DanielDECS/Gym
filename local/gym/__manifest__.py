{
    'name': 'Gym Management System',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manages gym clients, instructors, and training sessions.',
    'author': 'Daniel Soares',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_partner_view.xml',
        'views/gym_specialty_view.xml',
        'views/gym_exercise_view.xml',
        'views/gym_menu.xml',
    ],
    'installable': True,
    'application': True,
}
