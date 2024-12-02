========================
device.umbrella.overview
========================


Operation: GET /dataservice/device/umbrella/overview
----------------------------------------------------


Get Umbrella overview from device

.. code:: python

    def get_umbrella_overview(device_id: str) -> Any: ...


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
        client.device.umbrella.overview.get_umbrella_overview()


