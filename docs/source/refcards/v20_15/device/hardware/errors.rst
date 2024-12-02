======================
device.hardware.errors
======================


Operation: GET /dataservice/device/hardware/errors
--------------------------------------------------


Get hardware error list from device

.. code:: python

    def create_error_alarm_list() -> Any: ...


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
        client.device.hardware.errors.create_error_alarm_list()


