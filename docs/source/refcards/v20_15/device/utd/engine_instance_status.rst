=================================
device.utd.engine_instance_status
=================================


Operation: GET /dataservice/device/utd/engine-instance-status
-------------------------------------------------------------


Get UTD engine instance status from device (Real Time)

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
        client.device.utd.engine_instance_status.get()


