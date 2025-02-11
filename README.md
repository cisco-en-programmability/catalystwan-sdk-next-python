Cisco Catalyst WAN SDK 2.0
==========================

Welcome to the official documentation for the Cisco Catalyst WAN SDK, a package designed for creating simple and parallel automatic requests via the official SD-WAN Manager API.

Overview
--------

Cisco Catalyst WAN SDK serves as a multiple session handler (provider, provider as a tenant, tenant) and is environment-independent. You just need a connection to any SD-WAN Manager.

Supported Catalystwan WAN Server Versions
-----------------------------------------

- 20.15
- 20.16

Important Notice: Version Incompatibility
-----------------------------------------

Cisco Catalyst WAN SDK Version 2.0 Incompatibility with Legacy Versions
We are excited to announce the release of Cisco Catalyst WAN SDK version 2.0. 
This new version introduces a range of enhancements and features designed 
to improve performance and usability. However, it is important to note that version 2.0 
is not compatible with any previous legacy versions of the SDK.

Actions Recommended:
    Backup: Ensure you have backups of your current projects before attempting to upgrade.
    Review Documentation: Carefully review the updated documentation and release notes for guidance on migration and new features.
    Test Thoroughly: Test your projects thoroughly in a development environment before deploying version 2.0 in production.

We appreciate your understanding and cooperation as we continue to enhance the Cisco Catalyst WAN SDK. Should you have any questions or require assistance, please reach out through our support channels.

Thank you for your continued support and feedback!


Installation
------------

To install the SDK, run the following command:

```bash
pip install catalystwan
```

Supported Python Versions
-------------------------

Python >= 3.8


Getting Started
---------------

To execute SDK APIs, you need to create a `ApiClient`. Use the `create_client()` method to configure a session, perform authentication, and obtain a `ApiClient` instance in an operational state.

### Example Usage

Here's a quick example of how to use the SDK:

```python
from catalystwan.core import create_client

url = "example.com"
username = "admin"
password = "password123"

with create_client(url=url, username=username, password=password) as client:
    result = client.health.devices.get_devices_health()
    print(result)
```

If you need to preform more complex operations that require models, they can utilize an alias: `m`. 
```python

with create_client(...) as client:
    result = client.admin.aaa.update_aaa_config(
        client.admin.aaa.m.Aaa(
            accounting: True,
            admin_auth_order: False,
            audit_disable: False,
            auth_fallback: False,
            auth_order: ["local"]
        )
    )
    print(result)
```

Using an alias allows for easier access and management of models, simplifying workflows and improving efficiency. This approach helps streamline operations without requiring direct integration with underlying models, making them more user-friendly and scalable.
