======================
device.wlan.interfaces
======================


Operation: GET /dataservice/device/wlan/interfaces
--------------------------------------------------


Get WLAN interface from device

.. code:: python

    def get_wlan_interfaces(device_id: str) -> Any: ...


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
        client.device.wlan.interfaces.get_wlan_interfaces()


