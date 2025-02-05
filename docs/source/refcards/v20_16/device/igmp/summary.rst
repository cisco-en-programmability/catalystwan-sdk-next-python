===================
device.igmp.summary
===================


Operation: GET /dataservice/device/igmp/summary
-----------------------------------------------


Get IGMP summary from device

.. code:: python

    def create_igmp_summary(device_id: str) -> Any: ...


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
        client.device.igmp.summary.create_igmp_summary()


