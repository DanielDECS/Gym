from odoo import models, fields

class GymExercise(models.Model):
    # Model definition
    _name = 'gym.exercise'
    _description = 'Gym Exercise'

    # Multi-company support
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        required=True,
        index=True,
        default=lambda self: self.env.company
    )

    # Basic fields
    name = fields.Char(string='Exercise Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)

    # Difficulty level
    difficulty = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ], string='Difficulty')

    # Each exercise belongs to one specialty
    specialty_id = fields.Many2one(
        'gym.specialty',
        string='Specialty'
    )