=======================
device.voice.phone_info
=======================


Operation: GET /dataservice/device/voice/phoneInfo
--------------------------------------------------


Get phone registration info from device

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
        client.device.voice.phone_info.get()


