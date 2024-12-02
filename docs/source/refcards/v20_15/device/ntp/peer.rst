===============
device.ntp.peer
===============


Operation: GET /dataservice/device/ntp/peer
-------------------------------------------


Get NTP peer list from device (Real Time)

.. code:: python

    def create_peer_list(device_id: str) -> List[Any]: ...


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
        client.device.ntp.peer.create_peer_list()


