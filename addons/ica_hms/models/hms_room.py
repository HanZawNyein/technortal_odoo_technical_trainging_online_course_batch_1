from odoo import api, fields, models

class HmsRoom(models.Model):
    _name = 'hms.room' # hms_room
    _description = 'HmsRoom'

    name = fields.Char(required=True)
    type = fields.Selection([
        ('normal', 'Normal'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP'),
    ], default='normal')

    hotel_id = fields.Many2one('hms.hotel',required=True)
    currency_id = fields.Many2one('res.currency',related="hotel_id.currency_id")
    amount = fields.Monetary(currency_field='currency_id')
    active = fields.Boolean(default=True)
