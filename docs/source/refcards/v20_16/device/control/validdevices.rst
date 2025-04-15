===========================
device.control.validdevices
===========================


Operation: GET /dataservice/device/control/validdevices
-------------------------------------------------------


Get vmanage valid device list (Real Time)

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.device.control.validdevices.get()


