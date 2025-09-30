from odoo import models, fields

class GymSpecialty(models.Model):
    _name = 'gym.specialty'
    _description = 'Gym Specialty'

    name = fields.Char(string='Specialty Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)

    exercise_ids = fields.One2many('gym.exercise', 'specialty_id', string='Exercises')
