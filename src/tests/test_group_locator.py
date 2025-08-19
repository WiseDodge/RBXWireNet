import unittest
from unittest.mock import patch, MagicMock
from roblox_opencloud.group_locator import GroupLocatorClient
import os

class TestGroupLocator(unittest.TestCase):

    @patch('roblox_opencloud.api_client.requests.Session.request')
    def test_get_group_info_mock(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            'id': 254145,
            'displayName': 'Example Group',
            'description': 'A sample group description',
            'owner': 'users/16706224',
            'memberCount': 1000,
        }
        mock_request.return_value = mock_response

        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_info(group_id)
            print("Mocked API response data:", data)
            self.assertIsInstance(data, dict)
            self.assertEqual(data['id'], group_id)
            self.assertIn('displayName', data)
            self.assertIn('description', data)
            self.assertIn('owner', data)
            self.assertIn('memberCount', data)
        except Exception as e:
            self.fail(f"Mock API call failed: {e}")

    @patch('roblox_opencloud.api_client.requests.Session.request')
    def test_get_group_memberships_mock(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "data": [
                {"userId": 123, "role": "Member"},
                {"userId": 456, "role": "Admin"}
            ],
            "nextPageToken": None
        }
        mock_request.return_value = mock_response

        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_memberships(group_id)
            self.assertIsInstance(data, dict)
            self.assertIn("data", data)
            self.assertEqual(len(data["data"]), 2)
            self.assertEqual(data["data"][0]["userId"], 123)
        except Exception as e:
            self.fail(f"Mock memberships API call failed: {e}")

    @patch('roblox_opencloud.api_client.requests.Session.request')
    def test_get_group_roles_mock(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "groupRoles": [
                {"id": "1431036", "displayName": "Admin", "rank": 255, "memberCount": 1}
            ]
        }
        mock_request.return_value = mock_response

        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_roles(group_id)
            self.assertIn("groupRoles", data)
            self.assertEqual(data["groupRoles"][0]["displayName"], "Admin")
        except Exception as e:
            self.fail(f"Mock roles API call failed: {e}")

    @patch('roblox_opencloud.api_client.requests.Session.request')
    def test_get_group_join_requests_mock(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "joinRequests": [],
            "nextPageToken": None
        }
        mock_request.return_value = mock_response

        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_join_requests(group_id)
            self.assertIn("joinRequests", data)
        except Exception as e:
            self.fail(f"Mock join requests API call failed: {e}")

    def test_get_group_info_real_api(self):
        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_info(group_id)
            print("Real API response data:", data)
            self.assertIsInstance(data, dict)
            self.assertEqual(int(data['id']), group_id)
            self.assertIn('displayName', data)
            self.assertIn('description', data)
            self.assertIn('owner', data)
            self.assertIn('memberCount', data)
        except Exception as e:
            self.fail(f"Real API call failed: {e}")

    def test_get_group_memberships_real_api(self):
        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_memberships(group_id)
            print("Real API memberships response:", data)
            self.assertIsInstance(data, dict)
            self.assertIn("groupMemberships", data)
            self.assertIsInstance(data["groupMemberships"], list)
            # Check if there are memberships returned
            if data["groupMemberships"]:
                membership = data["groupMemberships"][0]
                self.assertIn("user", membership)
                self.assertIn("role", membership)
        except Exception as e:
            self.fail(f"Real memberships API call failed: {e}")

    def test_get_group_roles_real_api(self):
        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_roles(group_id)
            print("Real API roles response:", data)
            self.assertIsInstance(data, dict)
            self.assertIn("groupRoles", data)
            if data["groupRoles"]:
                role = data["groupRoles"][0]
                self.assertIn("displayName", role)
                self.assertIn("rank", role)
        except Exception as e:
            self.fail(f"Real roles API call failed: {e}")

    @unittest.skipUnless(
    os.getenv("RUN_JOIN_REQUESTS_TESTS", "").lower() == "true",
    "Insufficient permissions to test join requests"
    )

    def test_get_group_join_requests_real_api(self):
        client = GroupLocatorClient()
        group_id = 254145
        try:
            data = client.get_group_join_requests(group_id)
            print("Real API join requests response:", data)
            self.assertIsInstance(data, dict)
            self.assertIn("joinRequests", data)
        except Exception as e:
            if "403" in str(e) or "PERMISSION_DENIED" in str(e):
                self.skipTest("Insufficient permissions to test join requests (403).")
            else:
                self.fail(f"Real join requests API call failed: {e}")
