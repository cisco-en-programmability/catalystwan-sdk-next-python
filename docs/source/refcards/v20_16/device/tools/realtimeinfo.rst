=========================
device.tools.realtimeinfo
=========================


Operation: GET /dataservice/device/tools/realtimeinfo
-----------------------------------------------------


Get hardware real time info from device

.. code:: python

    def get_real_timeinfo(device_id: str) -> Any: ...


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
        client.device.tools.realtimeinfo.get_real_timeinfo()


