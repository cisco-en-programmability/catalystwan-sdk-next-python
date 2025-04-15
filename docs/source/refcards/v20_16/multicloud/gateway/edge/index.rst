=======================
multicloud.gateway.edge
=======================


Operation: GET /dataservice/multicloud/gateway/edge
---------------------------------------------------


Deprecated!!!

Get Interconnect Gateways

.. code:: python

    def get_icgws(
        edge_type: Optional[EdgeTypeParam] = None,
        account_id: Optional[str] = None,
        region: Optional[str] = None,
        region_id: Optional[str] = None,
        resource_state: Optional[str] = None,
        edge_gateway_name: Optional[str] = None,
        billing_account_id: Optional[str] = None,
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
        client.multicloud.gateway.edge.get_icgws()


Operation: POST /dataservice/multicloud/gateway/edge
----------------------------------------------------


Deprecated!!!

Create Interconnect Gateway

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.multicloud.gateway.edge.post()


Operation: GET /dataservice/multicloud/gateway/edge/{edgeGatewayName}
---------------------------------------------------------------------


Deprecated!!!

Get Interconnect Gateway by name

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
        client.multicloud.gateway.edge.get()


Operation: PUT /dataservice/multicloud/gateway/edge/{edgeGatewayName}
---------------------------------------------------------------------


Deprecated!!!

Update Interconnect Gateway

.. code:: python

    def put(
        edge_gateway_name: str, payload: UpdateIcgwPutRequest
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
        client.multicloud.gateway.edge.put()


Operation: DELETE /dataservice/multicloud/gateway/edge/{edgeGatewayName}
------------------------------------------------------------------------


Deprecated!!!

Delete Interconnect Gateway

.. code:: python

    def delete(edge_gateway_name: str) -> Any: ...


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
        client.multicloud.gateway.edge.delete()


.. toctree::
    :maxdepth: 1

    setting
    types/index
    models

