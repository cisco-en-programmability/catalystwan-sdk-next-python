===============================
multicloud.gateway.edge.setting
===============================


Operation: GET /dataservice/multicloud/gateway/edge/setting/{edgeGatewayName}
-----------------------------------------------------------------------------


Deprecated!!!

Get Interconnect Gateway custom setting by Interconnect Gateway name

.. code:: python

    def get(edge_gateway_name: str) -> Any: ...


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
        client.multicloud.gateway.edge.setting.get()


