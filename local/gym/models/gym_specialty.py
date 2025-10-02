from odoo import models, fields

class GymSpecialty(models.Model):
    _name = 'gym.specialty'           # Technical name of the model
    _description = 'Gym Specialty'    # Human-readable description

    name = fields.Char(string='Specialty Name', required=True)   # Name of the specialty
    description = fields.Text(string='Description')              # Description of the specialty
    active = fields.Boolean(default=True)                        # Used to archive/disable specialties

    # One specialty can have multiple exercises
    exercise_ids = fields.One2many(
        'gym.exercise',       # Target model
        'specialty_id',       # Inverse field in gym.exercise
        string='Exercises'
    )