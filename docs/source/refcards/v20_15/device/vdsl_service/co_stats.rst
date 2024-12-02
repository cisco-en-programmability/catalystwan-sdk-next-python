============================
device.vdsl_service.co_stats
============================


Operation: GET /dataservice/device/vdslService/coStats
------------------------------------------------------


Get CO stats from device

.. code:: python

    def get_co_stats(device_id: str) -> Any: ...


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
        client.device.vdsl_service.co_stats.get_co_stats()


