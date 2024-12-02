===============
device.csp.rbac
===============


Operation: GET /dataservice/device/csp/rbac
-------------------------------------------


Get RBAC interfaces from device

.. code:: python

    def get_rbac_interface(device_id: str) -> Any: ...


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
        client.device.csp.rbac.get_rbac_interface()


