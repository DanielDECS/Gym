from odoo import models, fields

class GymMember(models.Model):
    """
    Model representing a gym member. It inherits from res.partner to reuse
    standard fields like name, contact info, and address.
    """
    _inherit = 'res.partner' # Inherits fields (name, email, phone, etc.) from the Partner model
    _name = 'gym.member'
    _description = 'Gym Member'

    # CRITICAL FIX for Many2many conflict:
    # Overrides the 'channel_ids' field inherited from res.partner to ensure it uses
    # a unique relational table name, avoiding the 'same table and columns' TypeError.
    channel_ids = fields.Many2many(
        'mail.channel', 
        'mail_channel_member_partner',  # Use a unique M2M table name for members
        'partner_id', 
        'channel_id', 
        copy=False,
        string='Channels',
        help='Communication channels linked to this member.'
    )

    # Selection field for the type of membership
    membership_level = fields.Selection([
        ('basic', 'Basic'), 
        ('premium', 'Premium'), 
        ('vip', 'VIP'),
    ],
        string='Membership Level',
        required=True,
        default='basic',
        help='Membership level of the gym member.'
    )

    # Date fields to track the duration of the membership
    membership_start = fields.Date(
        string='Start Date', 
        required=True, 
        default=fields.Date.today(), 
        help='The date the membership started.'
    )
    
    membership_end = fields.Date(
        string='End Date',
        help='The date the membership expires.'
    )
    
    # Boolean flag to easily identify and filter members
    is_member = fields.Boolean(
        string='Is a Member', 
        default=True, 
        store=True, # Ensures the value is stored in the database
        help='Boolean flag indicating if the contact is an active member.'
    )