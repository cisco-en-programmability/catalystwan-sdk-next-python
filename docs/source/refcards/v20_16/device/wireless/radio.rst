=====================
device.wireless.radio
=====================


Operation: GET /dataservice/device/wireless/radio
-------------------------------------------------


Get wireless Radios from device

.. code:: python

    def get_wireless_radios(device_id: str) -> Any: ...


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
        client.device.wireless.radio.get_wireless_radios()


