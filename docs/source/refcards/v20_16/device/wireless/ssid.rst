====================
device.wireless.ssid
====================


Operation: GET /dataservice/device/wireless/ssid
------------------------------------------------


Get wireless SSID from device

.. code:: python

    def get_wireless_ssid(device_id: str) -> Any: ...


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
        client.device.wireless.ssid.get_wireless_ssid()


