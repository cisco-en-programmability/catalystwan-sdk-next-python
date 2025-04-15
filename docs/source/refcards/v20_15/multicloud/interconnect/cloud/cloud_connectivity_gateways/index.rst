=========================================================
multicloud.interconnect.cloud.cloud_connectivity_gateways
=========================================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways
--------------------------------------------------------------------------------------------------


API to retrieve all Cloud Connectivity Gateways.

.. code:: python

    def get(
        cloud_type: CloudTypeParam,
        cloud_account_id: str,
        connectivity_gateway_name: Optional[str] = None,
        connectivity_gateway_type: Optional[
            ConnectivityGatewayTypeParam
        ] = None,
        interconnect_type: Optional[InterconnectTypeParam] = None,
        region: Optional[str] = None,
        network: Optional[str] = None,
        resource_state: Optional[str] = None,
        refresh: Optional[str] = "false",
    ) -> InlineResponse2008: ...


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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.get()


Operation: POST /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways
---------------------------------------------------------------------------------------------------


API to create a Cloud Connectivity Gateway such as Direct Connect Gateway, Express Route Circuit or Google Cloud routers.

.. code:: python

    def post(
        cloud_type: CloudTypeParam, payload: CloudConnectivityGateway
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.post()


Operation: DELETE /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(
        cloud_type: CloudTypeParam,
        connectivity_gateway_type: Optional[
            ConnectivityGatewayTypeParam
        ] = None,
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.delete()


Operation: DELETE /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways/{connectivity-gateway-name}
---------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(
        connectivity_gateway_name: str,
        cloud_type: CloudTypeParam,
        connectivity_gateway_type: Optional[
            ConnectivityGatewayTypeParam
        ] = None,
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.delete()


.. toctree::
    :maxdepth: 1

    create_options/index
    models

