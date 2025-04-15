====================================
multicloud.devicelink.edge.portspeed
====================================


Operation: GET /dataservice/multicloud/devicelink/edge/portspeed/{edgeType}
---------------------------------------------------------------------------


Deprecated!!!

Get supported port speed for Device Link

.. code:: python

    def get(edge_type: EdgeTypeParam) -> Any: ...


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
        client.multicloud.devicelink.edge.portspeed.get()


.. toctree::
    :maxdepth: 1

    models

