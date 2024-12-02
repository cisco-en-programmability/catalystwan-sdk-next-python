==============================
multicloud.connectivitygateway
==============================


Operation: GET /dataservice/multicloud/connectivitygateway
----------------------------------------------------------


Deprecated!!!

Get all Connectivity Gateways

.. code:: python

    def get_connectivity_gateways(
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
        client.multicloud.connectivitygateway.get_connectivity_gateways()


Operation: POST /dataservice/multicloud/connectivitygateway
-----------------------------------------------------------


Deprecated!!!

Create Connectivity gateway

.. code:: python

    def create_connectivity_gateway(
        payload: Optional[Any] = None,
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
        client.multicloud.connectivitygateway.create_connectivity_gateway()


Operation: DELETE /dataservice/multicloud/connectivitygateway
-------------------------------------------------------------


Deprecated!!!

Delete all Connectivity Gateways in local DB

.. code:: python

    def clean_up_all_connectivity_gateways_in_local_db(
        deletion_type: Optional[str] = None,
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
        client.multicloud.connectivitygateway.clean_up_all_connectivity_gateways_in_local_db()


Operation: DELETE /dataservice/multicloud/connectivitygateway/{cloudProvider}/{connectivityGatewayName}
-------------------------------------------------------------------------------------------------------


Deprecated!!!

Delete Connectivity Gateway

.. code:: python

    def delete_connectivity_gateway(
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
        client.multicloud.connectivitygateway.delete_connectivity_gateway()


.. toctree::
    :maxdepth: 1

    models

