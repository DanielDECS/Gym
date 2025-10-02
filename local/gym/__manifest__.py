{
    'name': 'Gym Management System',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manages gym clients, instructors, and training sessions.',
    'author': 'Daniel Soares',
    'license': 'LGPL-3', # Explicit license
    'depends': ['base'], # Depends on the base Odoo module
    'data': [
        'security/ir.model.access.csv',  # Access control for our models
        'views/gym_partner_view.xml',    # Views for members and instructors
        'views/gym_specialty_view.xml',  # Specialty views
        'views/gym_exercise_view.xml',   # Exercise views
        'views/gym_menu.xml',            # Main menu structure
    ],
    'installable': True,   # Module can be installed
    'application': True,   # Show in main Odoo apps menu
}
