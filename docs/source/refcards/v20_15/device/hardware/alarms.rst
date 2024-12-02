======================
device.hardware.alarms
======================


Operation: GET /dataservice/device/hardware/alarms
--------------------------------------------------


Get hardware alarm list from device

.. code:: python

    def create_alarm_list(device_id: str) -> Any: ...


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
        client.device.hardware.alarms.create_alarm_list()


