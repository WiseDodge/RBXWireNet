# RBXWireNet Project Directory Tree

```
RBXWireNet/                     # Project root folder
├── .gitignore
├── directoryinROOT.txt
├── README.md
├── requirements.txt
├── setup.py
│
├── .github/                    # GitHub configuration
│   └── workflows/
│       ├── discord-notify.yml
│       └── python-app.yml
│
├── docs/                       # Documentation folder
│   ├── CHANGELOG.md
│   ├── DirectoryTree.md
│   └── PLANS.md
│
└── src/                        # Source code root
    ├── main.py
    │
    ├── RBXWireNet.egg-info/    # Package metadata (ignored in git)
    │   ├── dependency_links.txt
    │   ├── PKG-INFO
    │   ├── requires.txt
    │   ├── SOURCES.txt
    │   └── top_level.txt
    │
    ├── roblox_opencloud/       # Core Python package
    │   ├── __init__.py          # Package initialization
    │   ├── api_client.py
    │   ├── config.py
    │   ├── game_data.py
    │   ├── group_locator.py
    │   ├── user_data.py
    │   └── utils.py
    │
    └── tests/                  # Unit and integration tests
        ├── __init__.py
        ├── test_api_client.py
        ├── test_group_locator.py
        └── test_user_data.py

```

---
