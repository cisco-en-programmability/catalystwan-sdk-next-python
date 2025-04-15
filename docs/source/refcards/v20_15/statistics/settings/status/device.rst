=================================
statistics.settings.status.device
=================================


Operation: GET /dataservice/statistics/settings/status/device
-------------------------------------------------------------


Get list of enabled device for statistics index

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.statistics.settings.status.device.get()


