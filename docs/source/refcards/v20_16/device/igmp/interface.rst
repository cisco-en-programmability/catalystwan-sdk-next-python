=====================
device.igmp.interface
=====================


Operation: GET /dataservice/device/igmp/interface
-------------------------------------------------


Get IGMP interface list from device

.. code:: python

    def create_igmp_interface_list(device_id: str) -> List[Any]: ...


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
        client.device.igmp.interface.create_igmp_interface_list()


