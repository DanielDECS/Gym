{
    'name': 'Gym Management System',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manages gym clients, instructors, and training sessions.',
    'author': 'Daniel Soares',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_specialty_views.xml',
        'views/gym_exercise_views.xml',
        'views/gym_instructor_views.xml',
        'views/gym_member_views.xml',
        'views/gym_menu.xml',
    ],
    'installable': True,
    'application': True,
}
