===============================
device.voiceisdninfo.isdnstatus
===============================


Operation: GET /dataservice/device/voiceisdninfo/isdnstatus
-----------------------------------------------------------


Retrieve Voice ISDN Status from device

.. code:: python

    def get_t1e1_isdn_status(device_id: str) -> Any: ...


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
        client.device.voiceisdninfo.isdnstatus.get_t1e1_isdn_status()


