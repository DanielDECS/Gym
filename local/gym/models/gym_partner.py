from odoo import models, fields

class GymPartner(models.Model):
    # Main partner model for the gym
    _name = 'gym.partner'
    _description = 'Gym Partner'

    # Flags to identify type of partner
    is_instructor = fields.Boolean(string='Is Instructor', default=False)
    is_member = fields.Boolean(string='Is Member', default=False)

    # Common fields
    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    # Instructor-specific fields
    specialty_id = fields.Many2one(
        'gym.specialty',
        string='Specialty'   # Each instructor can have one specialty
    )
    hire_date = fields.Date(string='Hire Date')          # Instructor hiring date
    salary_rate = fields.Float(string='Hourly Rate')     # Salary rate for instructor

    # Member-specific fields
    level = fields.Selection([
        ('basic','Basic'),
        ('premium','Premium'),
        ('vip','VIP')
    ], string='Membership Level')                                 # Membership type/level
    membership_start = fields.Date(string='Membership Start')     # Start date of membership
    membership_end = fields.Date(string='Membership End')         # End date of membership

    # Relation: Members ↔ Instructors
    instructor_ids = fields.Many2many(
        'gym.partner',                     # Self-relation model
        'gym_member_instructor_rel',       # Relation table name
        'member_id',                       # Column linking to member
        'instructor_id',                   # Column linking to instructor
        string='Instructors',
        domain=[('is_instructor', '=', True)]  # Only show partners marked as instructors
    )
