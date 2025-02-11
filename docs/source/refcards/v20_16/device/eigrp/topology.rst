=====================
device.eigrp.topology
=====================


Operation: GET /dataservice/device/eigrp/topology
-------------------------------------------------


Get EIGRP topology info from device (Real Time)

.. code:: python

    def create_eigrp_topology(device_id: str) -> Any: ...


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
        client.device.eigrp.topology.create_eigrp_topology()


