from odoo import models, fields

class GymExercise(models.Model):
    _name = 'gym.exercise'
    _description = 'Gym Exercise'

    name = fields.Char(string='Exercise Name', required=True)
    specialty_id = fields.Many2one('gym.specialty', string='Specialty')
    description = fields.Text(string='Description')
    difficulty = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], string='Difficulty')
    active = fields.Boolean(string='Active', default=True)