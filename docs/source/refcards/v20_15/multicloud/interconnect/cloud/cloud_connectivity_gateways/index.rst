=========================================================
multicloud.interconnect.cloud.cloud_connectivity_gateways
=========================================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways
--------------------------------------------------------------------------------------------------


API to retrieve all Cloud Connectivity Gateways.

.. code:: python

    def get_cloud_connectivity_gateways(
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.get_cloud_connectivity_gateways()


Operation: POST /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways
---------------------------------------------------------------------------------------------------


API to create a Cloud Connectivity Gateway such as Direct Connect Gateway, Express Route Circuit or Google Cloud routers.

.. code:: python

    def add_cloud_connectivity_gateway(
        cloud_type: CloudTypeParam,
        payload: Optional[CloudConnectivityGateway] = None,
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.add_cloud_connectivity_gateway()


Operation: DELETE /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways
-----------------------------------------------------------------------------------------------------


API to delete Cloud Connectivity Gateways by type.

.. code:: python

    def delete_cloud_connectivity_gateways(
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.delete_cloud_connectivity_gateways()


Operation: DELETE /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways/{connectivity-gateway-name}
---------------------------------------------------------------------------------------------------------------------------------


API to delete a Cloud Connectivity Gateway.

.. code:: python

    def delete_cloud_connectivity_gateway(
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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.delete_cloud_connectivity_gateway()


.. toctree::
    :maxdepth: 1

    create_options/index
    models

