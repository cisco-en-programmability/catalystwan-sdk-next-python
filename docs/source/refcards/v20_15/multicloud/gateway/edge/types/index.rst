=============================
multicloud.gateway.edge.types
=============================


Operation: GET /dataservice/multicloud/gateway/edge/types
---------------------------------------------------------


Deprecated!!!

Get Interconnect Gateway type for specified Edge Provider

.. code:: python

    def get(edge_type: Optional[EdgeTypeParam] = None) -> Any: ...


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
        client.multicloud.gateway.edge.types.get()


.. toctree::
    :maxdepth: 1

    models

