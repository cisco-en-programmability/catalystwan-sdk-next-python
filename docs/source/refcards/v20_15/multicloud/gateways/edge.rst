========================
multicloud.gateways.edge
========================


Operation: GET /dataservice/multicloud/gateways/edge/{edgeType}
---------------------------------------------------------------


Deprecated!!!

Get sites with connectivity to the interconnect gateways by edge type

.. code:: python

    def get_edge_gateways(edge_type: str) -> Any: ...


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
        client.multicloud.gateways.edge.get_edge_gateways()


