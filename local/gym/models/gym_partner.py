from odoo import models, fields

class GymPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Is Instructor', default=False)
    is_member = fields.Boolean(string='Is Member', default=False)

    # Instructor
    specialty_ids = fields.Many2many(
        'gym.specialty', 
        'gym_instructor_specialty_rel',
        'instructor_id', 'specialty_id', 
        string='Specialties'
    )
    hire_date = fields.Date(string='Hire Date')
    salary_rate = fields.Float(string='Hourly Rate')

    # Member
    membership_level = fields.Selection([
        ('basic','Basic'),
        ('premium','Premium'),
        ('vip','VIP')
    ], string='Membership Level')
    membership_start = fields.Date(string='Membership Start')
    membership_end = fields.Date(string='Membership End')
    instructor_ids = fields.Many2many(
        'res.partner', 
        'gym_member_instructor_rel',
        'member_id', 'instructor_id',
        string='Instructors',
        domain=[('is_instructor', '=', True)]
    )
