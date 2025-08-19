from roblox_opencloud.group_locator import GroupLocatorClient


def main():
    client = GroupLocatorClient()
    group_id = int(input("Enter Roblox Group ID: "))
    try:
        group_info = client.get_group_info(group_id)
        print("Group Info:", group_info)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
