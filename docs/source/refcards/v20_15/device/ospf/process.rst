===================
device.ospf.process
===================


Operation: GET /dataservice/device/ospf/process
-----------------------------------------------


Get OSPF process list from device (Real Time)

.. code:: python

    def create_ospf_process(device_id: str) -> List[Any]: ...


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
        client.device.ospf.process.create_ospf_process()


