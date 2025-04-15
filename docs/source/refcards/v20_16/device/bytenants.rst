================
device.bytenants
================


Operation: GET /dataservice/device/bytenants
--------------------------------------------


Gets devices and sites for all tenants

.. code:: python

    def get(tenant: Optional[List[str]] = None) -> None: ...


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
        client.device.bytenants.get()


