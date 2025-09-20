from odoo import api, fields, models

class HmsHotel(models.Model):
    _name = 'hms.hotel'
    _inherit = ['image.mixin']
    _description = 'HmsHotel'

    name = fields.Char()
    room_ids = fields.One2many('hms.room', 'hotel_id')
    currency_id = fields.Many2one('res.currency',required=True)