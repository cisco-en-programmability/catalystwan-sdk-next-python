============================
device.tunnel.bfd_statistics
============================


Operation: GET /dataservice/device/tunnel/bfd_statistics
--------------------------------------------------------


Get tunnel BFD statistics all devices

.. code:: python

    def create_bfd_statistics_list(device_id: str) -> Any: ...


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
        client.device.tunnel.bfd_statistics.create_bfd_statistics_list()


