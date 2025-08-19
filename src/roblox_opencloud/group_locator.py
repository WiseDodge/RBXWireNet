from .api_client import APIClient


class GroupLocatorClient:
    def __init__(self, api_client=None):
        self.api_client = api_client or APIClient()
        self.endpoint = "groups/"  # updated endpoint path for Cloud v2 API


    def get_group_info(self, group_id):
        endpoint = f"{self.endpoint}{group_id}"
        return self.api_client.get(endpoint)

    def get_group_memberships(self, group_id, max_page_size=10, page_token=None):
        endpoint = f"{self.endpoint}{group_id}/memberships?maxPageSize={max_page_size}"
        if page_token:
            endpoint += f"&pageToken={page_token}"
        return self.api_client.get(endpoint)

    def get_group_roles(self, group_id):
        endpoint = f"{self.endpoint}{group_id}/roles"
        return self.api_client.get(endpoint)

    def get_group_join_requests(self, group_id, max_page_size=20, page_token=None):
        endpoint = f"{self.endpoint}{group_id}/join-requests?maxPageSize={max_page_size}"
        if page_token:
            endpoint += f"&pageToken={page_token}"
        return self.api_client.get(endpoint)

