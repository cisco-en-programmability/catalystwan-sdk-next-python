==========================
system.device.decommission
==========================


Operation: PUT /dataservice/system/device/decommission/{uuid}
-------------------------------------------------------------


Decomission vEdge device

.. code:: python

    def put(uuid: str) -> DecommissionVedgeCloud: ...


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
        client.system.device.decommission.put()


.. toctree::
    :maxdepth: 1

    models

