======================
device.ondemand.remote
======================


Operation: GET /dataservice/device/ondemand/remote
--------------------------------------------------


Get on-demand remote (Real Time)

.. code:: python

    def get_on_demand_remote(device_id: str) -> List[Any]: ...


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
        client.device.ondemand.remote.get_on_demand_remote()


