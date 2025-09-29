from odoo import models, fields

class GymInstructor(models.Model):
    """
    Model representing a gym instructor. It inherits from res.partner to reuse
    standard fields like name, contact info, and address.
    """
    _inherit = 'res.partner'
    _name = 'gym.instructor'
    _description = 'Gym Instructor'

    # CRITICAL FIX for Many2many conflict:
    # Overrides the 'channel_ids' field inherited from res.partner to ensure it uses
    # a unique relational table name, avoiding the 'same table and columns' TypeError.
    channel_ids = fields.Many2many(
        'mail.channel', 
        'mail_channel_instructor_partner',  # Unique M2M table name
        'partner_id', 
        'channel_id', 
        copy=False,
        string='Channels',
        help='Communication channels linked to this instructor.'
    )

    # Many2many field linking the instructor to multiple specialties they teach.
    specialty_ids = fields.Many2many(
        comodel_name='gym.specialty',
        relation='gym_instructor_specialty_rel', # Unique M2M table for specialties
        column1='instructor_id',
        column2='specialty_id',
        string='Specialties',
        help='The specialties this instructor teaches.'
    )
    
    # Custom fields for employment and payroll details
    hire_date = fields.Date(
        string='Hire Date', 
        default=fields.Date.today(),
        help='The date the instructor was hired.'
    )
    
    salary_rate = fields.Float(
        string='Hourly Rate',
        help='The hourly pay rate for the instructor.'
    )
    
    # Boolean flag to easily identify and filter instructors
    is_instructor = fields.Boolean(
        string='Is Instructor', 
        default=True,
        store=True, # Ensures the value is stored in the database
        help='Boolean flag indicating if the contact is an instructor.'
    )