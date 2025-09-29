from odoo import models, fields

class GymExercise(models.Model):
    """
    Model to define different types of exercises available in the gym.
    """
    _name = 'gym.exercise'
    _description = 'Gym Exercise'

    # Basic data fields
    name = fields.Char(
        string='Exercise Name', 
        required=True,
        help='The official name of the exercise.'
    )
    
    # Relational field: Links the exercise to its corresponding specialty (e.g., Yoga, Cardio)
    specialty_id = fields.Many2one(
        'gym.specialty', 
        string='Specialty',
        help='The main training area this exercise belongs to.'
    )
    
    description = fields.Text(
        string='Description',
        help='Detailed description of how to perform the exercise.'
    )
    
    # Selection field with predefined options
    difficulty = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], 
        string='Difficulty',
        help='Level of difficulty for this exercise.'
    )
    
    active = fields.Boolean(
        string='Active', 
        default=True, # By default, the exercise is available
        help='If checked, the exercise is available for use.'
    )