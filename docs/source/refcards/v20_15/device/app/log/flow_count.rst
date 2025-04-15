=========================
device.app.log.flow_count
=========================


Operation: GET /dataservice/device/app/log/flow-count
-----------------------------------------------------


Get App log flows count from device (Real Time)

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
        client.device.app.log.flow_count.get()


