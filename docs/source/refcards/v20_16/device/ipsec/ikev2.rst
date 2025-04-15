==================
device.ipsec.ikev2
==================


Operation: GET /dataservice/device/ipsec/ikev2
----------------------------------------------


Get Crypto IKEv2 SA entry from device

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
        client.device.ipsec.ikev2.get()


