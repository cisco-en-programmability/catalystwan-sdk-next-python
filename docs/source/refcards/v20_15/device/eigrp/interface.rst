======================
device.eigrp.interface
======================


Operation: GET /dataservice/device/eigrp/interface
--------------------------------------------------


Get EIGRP interface list from device (Real Time)

.. code:: python

    def create_eigrp_interface(device_id: str) -> Any: ...


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
        client.device.eigrp.interface.create_eigrp_interface()


