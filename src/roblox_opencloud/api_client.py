import requests
from .config import RBXWIRENET_GROUP_API_KEY, BASE_URL


class APIClient:
    def __init__(self, base_url=BASE_URL, api_key=RBXWIRENET_GROUP_API_KEY):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": self.api_key,
            "Accept": "application/json"
        })


    def _request(self, method, endpoint, params=None):
        url = self.base_url + endpoint
        response = self.session.request(method, url, params=params)

        if not response.ok:
            raise Exception(f"API request failed: {response.status_code} {response.text}")

        return response.json()


    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params)


    def get_group_info(self, group_id):
        endpoint = f"groups/{group_id}"
        return self.get(endpoint)
