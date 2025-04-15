===============
topology.device
===============


Operation: GET /dataservice/topology/device
-------------------------------------------


Create device topology

.. code:: python

    def get(device_id: List[DeviceIp]) -> Any: ...


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
        client.topology.device.get()


.. toctree::
    :maxdepth: 1

    site
    models

