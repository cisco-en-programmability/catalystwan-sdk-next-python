============================
device.ospf.databaseexternal
============================


Operation: GET /dataservice/device/ospf/databaseexternal
--------------------------------------------------------


Get OSPF external database list from device (Real Time)

.. code:: python

    def create_ospf_database_external(device_id: str) -> List[Any]: ...


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
        client.device.ospf.databaseexternal.create_ospf_database_external()


