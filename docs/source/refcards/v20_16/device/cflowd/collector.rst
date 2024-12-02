=======================
device.cflowd.collector
=======================


Operation: GET /dataservice/device/cflowd/collector
---------------------------------------------------


Get cflowd collector list from device

.. code:: python

    def create_cflowd_collector_list(device_id: str) -> List[Any]: ...


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
        client.device.cflowd.collector.create_cflowd_collector_list()


