==============================
multicloud.connectivitygateway
==============================


Operation: GET /dataservice/multicloud/connectivitygateway
----------------------------------------------------------


Deprecated!!!

Get all Connectivity Gateways

.. code:: python

    def get(
        account_id: Optional[str] = None,
        cloud_type: Optional[str] = None,
        connectivity_type: Optional[str] = None,
        connectivity_gateway_name: Optional[str] = None,
        region: Optional[str] = None,
        network: Optional[str] = None,
        state: Optional[str] = None,
        refresh: Optional[str] = None,
        edge_type: Optional[EdgeTypeParam] = None,
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
        client.multicloud.connectivitygateway.get()


Operation: POST /dataservice/multicloud/connectivitygateway
-----------------------------------------------------------


Deprecated!!!

Create Connectivity gateway

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
        client.multicloud.connectivitygateway.post()


Operation: DELETE /dataservice/multicloud/connectivitygateway
-------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def delete(deletion_type: Optional[str] = None) -> Any: ...


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
        client.multicloud.connectivitygateway.delete()


Operation: DELETE /dataservice/multicloud/connectivitygateway/{cloudProvider}/{connectivityGatewayName}
-------------------------------------------------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def delete(
        cloud_provider: str,
        connectivity_gateway_name: str,
        connectivity_type: Optional[str] = None,
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
        client.multicloud.connectivitygateway.delete()


.. toctree::
    :maxdepth: 1

    models

