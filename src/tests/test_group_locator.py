import unittest
from roblox_opencloud.group_locator import GroupLocatorClient

class TestGroupLocator(unittest.TestCase):
    def test_get_group_info(self):
        client = GroupLocatorClient()
        # Example group ID - replace with a valid or mock value
        group_id = 0  
        try:
            data = client.get_group_info(group_id)
            self.assertIsInstance(data, dict)
        except Exception as e:
            self.fail(f"API call failed: {e}")
