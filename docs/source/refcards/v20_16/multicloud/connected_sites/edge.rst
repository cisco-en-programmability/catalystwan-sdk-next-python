===============================
multicloud.connected_sites.edge
===============================


Operation: GET /dataservice/multicloud/connected-sites/edge/{edgeType}
----------------------------------------------------------------------


Deprecated!!!

Get sites with connectivity to the interconnect gateways by edge type

.. code:: python

    def get(
        edge_type: str, edge_gateway_name: Optional[str] = None
    ) -> Any: ...


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
        client.multicloud.connected_sites.edge.get()


