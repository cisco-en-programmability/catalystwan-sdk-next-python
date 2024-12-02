=========================
device.control.statistics
=========================


Operation: GET /dataservice/device/control/statistics
-----------------------------------------------------


Get connection statistics from device (Real Time)

.. code:: python

    def get_connection_statistics(device_id: str) -> Any: ...


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
        client.device.control.statistics.get_connection_statistics()


