from odoo import models, fields, api
from .easy_delivery_api import EasyDeliveryAPI


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    easy_delivery_tracking = fields.Char('Tracking Number')
    easy_delivery_label = fields.Binary('Shipping Label')

    def action_generate_easy_delivery_label(self):
        self.ensure_one()
        carrier = self.carrier_id

        api = EasyDeliveryAPI(
            carrier.easy_delivery_api_key,
            carrier.easy_delivery_api_secret,
            carrier.easy_delivery_api_url
        )

        # Préparer les données d'expédition
        shipment_data = self._prepare_easy_delivery_shipment()

        # Créer l'expédition
        response = api.create_shipment(shipment_data)

        # Sauvegarder le numéro de suivi
        self.easy_delivery_tracking = response['tracking_number']

        # Récupérer l'étiquette ZPL
        label_data = api.get_label(response['shipment_id'])
        self.easy_delivery_label = label_data['zpl_content']

        return True

    def _prepare_easy_delivery_shipment(self):
        return {
            'recipient': {
                'name': self.partner_id.name,
                'address': self.partner_id.street,
                'city': self.partner_id.city,
                'zip': self.partner_id.zip,
                'country': self.partner_id.country_id.code,
            },
            'packages': [{
                'weight': self.shipping_weight,
                'dimensions': {
                    'length': self.package_ids.length,
                    'width': self.package_ids.width,
                    'height': self.package_ids.height
                }
            }]
        }
