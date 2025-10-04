from odoo import models, fields

class GymPartner(models.Model):
    _name = 'gym.partner'
    _description = 'Gym Partner'

    # Multi-company support
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        required=True,
        index=True,
        default=lambda self: self.env.company
    )

    # Flags to identify type of partner
    is_instructor = fields.Boolean(string='Is Instructor', default=False)
    is_member = fields.Boolean(string='Is Member', default=False)

    # Common fields
    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    image_1920 = fields.Image(string="Image")  # Partner photo

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
    ], string='Membership Level')
    membership_start = fields.Date(string='Membership Start')     # Start date of membership
    membership_end = fields.Date(string='Membership End')         # End date of membership

    # Relation: Members ↔ Instructors
    instructor_ids = fields.Many2many(
        'gym.partner',
        'gym_member_instructor_rel',
        'member_id',
        'instructor_id',
        string='Instructors',
        domain=[('is_instructor', '=', True)] # Only show partners marked as instructors
    )
