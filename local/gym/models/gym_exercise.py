from odoo import models, fields

class GymExercise(models.Model):
    _name = 'gym.exercise'           # Technical name of the model
    _description = 'Gym Exercise'    # Human-readable description

    name = fields.Char(string='Exercise Name', required=True)  # Name of the exercise
    description = fields.Text(string='Description')            # Description of the exercise

    # Each exercise belongs to one specialty
    specialty_id = fields.Many2one(
        'gym.specialty',                         # Target model
        string='Specialty'
    )

    # Difficulty level of the exercise
    difficulty = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ], string='Difficulty')

    active = fields.Boolean(default=True)     # Used to archive/disable exercises
