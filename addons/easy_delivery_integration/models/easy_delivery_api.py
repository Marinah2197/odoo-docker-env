import requests
import json


class EasyDeliveryAPI:
    def __init__(self, api_key, api_secret, api_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_url = api_url

    def create_shipment(self, shipment_data):
        headers = self._get_headers()
        response = requests.post(
            f"{self.api_url}/shipments",
            headers=headers,
            json=shipment_data
        )
        return response.json()

    def get_label(self, shipment_id):
        headers = self._get_headers()
        response = requests.get(
            f"{self.api_url}/shipments/{shipment_id}/label",
            headers=headers
        )
        return response.json()

    def _get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
