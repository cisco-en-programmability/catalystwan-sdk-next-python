=======================
device.voice.voip_calls
=======================


Operation: GET /dataservice/device/voice/voipCalls
--------------------------------------------------


Get VOIP call info from device

.. code:: python

    def get_voip_calls(device_id: str) -> Any: ...


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
        client.device.voice.voip_calls.get_voip_calls()


