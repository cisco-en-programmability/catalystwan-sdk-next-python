=====================
device.ondemand.local
=====================


Operation: GET /dataservice/device/ondemand/local
-------------------------------------------------


Get on-demand local (Real Time)

.. code:: python

    def get_on_demand_local(device_id: str) -> List[Any]: ...


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
        client.device.ondemand.local.get_on_demand_local()


