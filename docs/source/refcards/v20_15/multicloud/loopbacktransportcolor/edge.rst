======================================
multicloud.loopbacktransportcolor.edge
======================================


Operation: GET /dataservice/multicloud/loopbacktransportcolor/edge
------------------------------------------------------------------


Deprecated!!!

Get Edge Loopback Tunnel supported colors

.. code:: python

    def get() -> Any: ...


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
        client.multicloud.loopbacktransportcolor.edge.get()


