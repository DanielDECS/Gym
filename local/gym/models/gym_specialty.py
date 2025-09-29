from odoo import models, fields

class GymSpecialty(models.Model):
    """
    Model to classify different training specialties offered by the gym,
    such as Cardio, Weightlifting, Yoga, etc.
    """
    _name = 'gym.specialty'
    _description = 'Gym Specialty'

    # Basic data fields
    name = fields.Char(
        string='Specialty Name', 
        required=True,
        help='The name of the training category.'
    )
    
    # Relational field: Links this specialty to all related exercises (One-to-Many)
    # 'gym.exercise' is the target model; 'specialty_id' is the foreign key on the target model
    exercise_ids = fields.One2many(
        'gym.exercise', 
        'specialty_id', 
        string='Exercises',
        help='List of exercises associated with this specialty.'
    )
    
    description = fields.Text(
        string='Description',
        help='Detailed description of the specialty.'
    )
    
    active = fields.Boolean(
        string='Active', 
        default=True,
        help='If checked, the specialty is currently offered by the gym.'
    )