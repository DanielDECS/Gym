from odoo import models, fields

class GymSpecialty(models.Model):
    # Model definition
    _name = 'gym.specialty'
    _description = 'Gym Specialty'

    # Multi-company support
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        required=True,
        index=True,
        default=lambda self: self.env.company
    )
    
    # Basic fields
    name = fields.Char(string='Specialty Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)

    # One specialty can have multiple exercises
    exercise_ids = fields.One2many(
        'gym.exercise',
        'specialty_id',
        string='Exercises'
    )
