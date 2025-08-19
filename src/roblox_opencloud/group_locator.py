from .api_client import APIClient

class GroupLocatorClient:
    def __init__(self, api_client=None):
        self.api_client = api_client or APIClient()
        self.endpoint = "/group_locator/v1/groups/"

    def get_group_info(self, group_id):
        endpoint = f"{self.endpoint}{group_id}"
        return self.api_client.get(endpoint)
