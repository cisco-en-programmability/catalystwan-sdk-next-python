==========================
dca.data.device.statistics
==========================


Operation: POST /dataservice/dca/data/device/statistics/{stats_data_type}
-------------------------------------------------------------------------


Get device statistics data

.. code:: python

    def post(stats_data_type: str, payload: Any) -> Any: ...


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
        client.dca.data.device.statistics.post()


