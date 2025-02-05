=====================================================================
multicloud.interconnect.connectivity.cloud_onramp_gateway_connections
=====================================================================


Operation: GET /dataservice/multicloud/interconnect/connectivity/cloud-onramp-gateway-connections
-------------------------------------------------------------------------------------------------


API to retrieve all Interconnect OnRamp gateway connection.

.. code:: python

    def get_interconnect_on_ramp_gateway_connections(
        cloud_type: Optional[str] = None,
        cloud_account_id: Optional[str] = None,
        connection_name: Optional[str] = None,
        refresh: Optional[str] = "false",
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
        client.multicloud.interconnect.connectivity.cloud_onramp_gateway_connections.get_interconnect_on_ramp_gateway_connections()


Operation: POST /dataservice/multicloud/interconnect/connectivity/cloud-onramp-gateway-connections
--------------------------------------------------------------------------------------------------


API to create an Interconnect OnRamp gateway connection.

.. code:: python

    def create_interconnect_on_ramp_gateway_connection(
        payload: List[
            CreateInterconnectOnRampGatewayConnectionPostRequest
        ],
    ) -> List[InterconnectOnRampGatewayConnection]: ...


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
        client.multicloud.interconnect.connectivity.cloud_onramp_gateway_connections.create_interconnect_on_ramp_gateway_connection()


Operation: GET /dataservice/multicloud/interconnect/connectivity/cloud-onramp-gateway-connections/{connection-name}
-------------------------------------------------------------------------------------------------------------------


API to retrieve a specific Interconnect OnRamp gateway connection.

.. code:: python

    def get_interconnect_on_ramp_gateway_connection(
        connection_name: str,
    ) -> InterconnectOnRampGatewayConnection: ...


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
        client.multicloud.interconnect.connectivity.cloud_onramp_gateway_connections.get_interconnect_on_ramp_gateway_connection()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/cloud-onramp-gateway-connections/{connection-name}
-------------------------------------------------------------------------------------------------------------------


API to update an Interconnect OnRamp gateway connection.

.. code:: python

    def update_interconnect_on_ramp_gateway_connection(
        connection_name: str,
        payload: UpdateInterconnectOnRampGatewayConnectionPutRequest,
    ) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.cloud_onramp_gateway_connections.update_interconnect_on_ramp_gateway_connection()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/cloud-onramp-gateway-connections/{connection-name}
----------------------------------------------------------------------------------------------------------------------


API to delete an Interconnect OnRamp gateway connection.

.. code:: python

    def delete_interconnect_on_ramp_gateway_connection(
        connection_name: str,
        delete_cloud_resources: Optional[str] = "false",
    ) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.cloud_onramp_gateway_connections.delete_interconnect_on_ramp_gateway_connection()


.. toctree::
    :maxdepth: 1

    models

