=========================
device.ip.nat.translation
=========================


Operation: GET /dataservice/device/ip/nat/translation
-----------------------------------------------------


Get NAT translation list from device (Real Time)

.. code:: python

    def create_nat_translation_list(device_id: str) -> Any: ...


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
        client.device.ip.nat.translation.create_nat_translation_list()


