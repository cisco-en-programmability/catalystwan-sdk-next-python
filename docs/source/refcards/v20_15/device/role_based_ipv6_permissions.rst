==================================
device.role_based_ipv6_permissions
==================================


Operation: GET /dataservice/device/roleBasedIpv6Permissions
-----------------------------------------------------------


get Cisco TrustSec Role Based ipv6 Permissions information from device

.. code:: python

    def get_role_based_ipv6_permissions(device_id: str) -> Any: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.device.role_based_ipv6_permissions.get_role_based_ipv6_permissions()


