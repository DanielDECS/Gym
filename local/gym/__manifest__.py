{
    'name': 'Gym Management System',
    'version': '1.1',
    'category': 'Services',
    'summary': 'Gym management with members, instructors, specialties, and exercises',
    'description': """
        A simple gym management system with multi-company support.
        - Manage Members
        - Manage Instructors
        - Manage Specialties
        - Manage Exercises
    """,
    'author': 'Daniel Soares',
    'license': 'LGPL-3', 
    'depends': ['base', 'web',],  
    'data': [
        'security/ir.model.access.csv',    # Access control
        'security/gym_security.xml',       # Security rules
        'views/gym_partner_views.xml',     # Views for members and instructors
        'views/gym_specialty_views.xml',   # Specialty views
        'views/gym_exercise_views.xml',    # Exercise views
        'views/gym_menus.xml',             # Menu structure
    ],
    'installable': True,
    'application': True,
}



