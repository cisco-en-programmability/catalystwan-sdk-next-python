================================
device.control.regionconnections
================================


Operation: GET /dataservice/device/control/regionconnections
------------------------------------------------------------


Get connections list from device (Real Time)

.. code:: python

    def create_real_time_region_connection_list(
        device_id: str,
    ) -> Any: ...


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
        client.device.control.regionconnections.create_real_time_region_connection_list()


