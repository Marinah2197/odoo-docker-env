from odoo import models, fields, api


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[
        ('easy_delivery', 'Easy Delivery')
    ])
    easy_delivery_api_key = fields.Char('API Key')
    easy_delivery_api_secret = fields.Char('API Secret')
    easy_delivery_api_url = fields.Char('API URL', default='https://api.easy-delivery.com/v1')
