======================
device.control.summary
======================


Operation: GET /dataservice/device/control/summary
--------------------------------------------------


Get connections summary from device (Real Time)

.. code:: python

    def create_connections_summary(device_id: str) -> Any: ...


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
        client.device.control.summary.create_connections_summary()


.. toctree::
    :maxdepth: 1

    device

