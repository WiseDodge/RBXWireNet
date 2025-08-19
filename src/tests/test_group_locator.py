import unittest
from unittest.mock import patch, MagicMock
from roblox_opencloud.group_locator import GroupLocatorClient


class TestGroupLocator(unittest.TestCase):

    @patch('roblox_opencloud.api_client.requests.Session.request')
    def test_get_group_info_mock(self, mock_request):
        # Mocking API response
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
            self.assertIsInstance(data, dict, "API response is not a dictionary")
            self.assertEqual(data['id'], group_id, "Group ID does not match expected")
            self.assertIn('displayName', data, "API response missing displayName")
            self.assertIn('description', data, "API response missing description")
            self.assertIn('owner', data, "API response missing owner")
            self.assertIn('memberCount', data, "API response missing memberCount")
        except Exception as e:
            self.fail(f"Mock API call failed: {e}")

    def test_get_group_info_real_api(self):
        client = GroupLocatorClient()
        group_id = 254145  # Testing real API call with a known group ID
        try:
            data = client.get_group_info(group_id)
            print("Real API response data:", data)
            self.assertIsInstance(data, dict, "API response is not a dictionary")
            # Checks if the group ID matches
            self.assertEqual(int(data['id']), group_id, "Group ID does not match expected")
            self.assertIn('displayName', data, "API response missing displayName")
            self.assertIn('description', data, "API response missing description")
            self.assertIn('owner', data, "API response missing owner")
            self.assertIn('memberCount', data, "API response missing memberCount")
        except Exception as e:
            self.fail(f"Real API call failed: {e}")
