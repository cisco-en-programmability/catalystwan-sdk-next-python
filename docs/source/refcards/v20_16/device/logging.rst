==============
device.logging
==============


Operation: GET /dataservice/device/logging
------------------------------------------


Get logging from device (Real Time)

.. code:: python

    def get_logging_from_device(device_id: str) -> List[Any]: ...


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
        client.device.logging.get_logging_from_device()


