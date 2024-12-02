=======================
device.ospf.v3interface
=======================


Operation: GET /dataservice/device/ospf/v3interface
---------------------------------------------------


Get OSPF v3 interface list from device (Real Time)

.. code:: python

    def create_osp_fv3_interface(device_id: str) -> List[Any]: ...


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
        client.device.ospf.v3interface.create_osp_fv3_interface()


