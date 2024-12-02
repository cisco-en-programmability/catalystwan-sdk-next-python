====================
device.multicast.rpf
====================


Operation: GET /dataservice/device/multicast/rpf
------------------------------------------------


Get RPF list from device

.. code:: python

    def create_rpf_list(device_id: str) -> Any: ...


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
        client.device.multicast.rpf.create_rpf_list()


