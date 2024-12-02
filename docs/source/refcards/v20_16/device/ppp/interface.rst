====================
device.ppp.interface
====================


Operation: GET /dataservice/device/ppp/interface
------------------------------------------------


Get PPP interface list from device (Real Time)

.. code:: python

    def create_ppp_interface_list(device_id: str) -> List[Any]: ...


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
        client.device.ppp.interface.create_ppp_interface_list()


