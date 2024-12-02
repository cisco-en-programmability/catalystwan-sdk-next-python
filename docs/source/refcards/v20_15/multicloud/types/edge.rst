=====================
multicloud.types.edge
=====================


Operation: GET /dataservice/multicloud/types/edge
-------------------------------------------------


Deprecated!!!

Get edge types

.. code:: python

    def get_edge_types() -> Any: ...


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
        client.multicloud.types.edge.get_edge_types()


