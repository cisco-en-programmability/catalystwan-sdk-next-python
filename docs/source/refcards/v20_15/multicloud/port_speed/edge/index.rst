==========================
multicloud.port_speed.edge
==========================


Operation: GET /dataservice/multicloud/portSpeed/edge/{edgeType}/{edgeAccountId}/{connectivityType}
---------------------------------------------------------------------------------------------------


Deprecated!!!

Get supported port speed

.. code:: python

    def get(
        edge_type: EdgeTypeParam,
        edge_account_id: str,
        connectivity_type: str,
        cloud_type: Optional[CloudTypeParam] = None,
        cloud_account_id: Optional[str] = None,
        connect_type: Optional[str] = None,
        connect_sub_type: Optional[str] = None,
        connectivity_gateway: Optional[str] = None,
        partner_port: Optional[str] = None,
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
        client.multicloud.port_speed.edge.get()


.. toctree::
    :maxdepth: 1

    models

