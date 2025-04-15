===========================
device.control.validvsmarts
===========================


Operation: GET /dataservice/device/control/validvsmarts
-------------------------------------------------------


Get valid vSmart list from device (Real Time)

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
        client.device.control.validvsmarts.get()


