====================
stream.device.status
====================


Operation: POST /dataservice/stream/device/status/{deviceUUID}
--------------------------------------------------------------


Get device status stream

.. code:: python

    def process_device_status(
        device_uuid: str, payload: Optional[str] = None
    ) -> None: ...


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
        client.stream.device.status.process_device_status()


