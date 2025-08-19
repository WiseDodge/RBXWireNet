# Changelog

All notable changes to the RBXWireNet project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Initial project scaffolding and setup including main script and modular package structure.
- Implemented generic API client (`APIClient`) with authentication and HTTP request handling.
- Added `GroupLocatorClient` for querying group data using Roblox Cloud v2 API (`groups/{group_id}` endpoint).
- Included environment variable (`RBXWIRENET_GROUP_API_KEY`) management via `.env` support for API key security.
- Created unit tests with mocks and integration tests for `GroupLocatorClient` covering both fake and real API responses.
- Prepared README.md with project overview, usage, tech stack, and configuration instructions.
- Established project plans in `PLANS.md` detailing roadmap and feature vision.

### Changed
- Updated base URL in config to target Roblox Cloud v2 API (`https://apis.roblox.com/cloud/v2/`).

### Fixed
- Corrected PEP 8 style issues with blank lines to pass flake8 lint checks across `main.py`, `api_client.py`, and `group_locator.py`.
  
### Removed
- (None so far)