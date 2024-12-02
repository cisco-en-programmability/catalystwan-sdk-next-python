=============================
device.role_based_permissions
=============================


Operation: GET /dataservice/device/roleBasedPermissions
-------------------------------------------------------


get Cisco TrustSec Role Based Permissions information from device

.. code:: python

    def get_role_based_permissions(device_id: str) -> Any: ...


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
        client.device.role_based_permissions.get_role_based_permissions()


