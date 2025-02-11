========================================================================
multicloud.interconnect.cloud.cloud_connectivity_gateways.create_options
========================================================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways/create-options
-----------------------------------------------------------------------------------------------------------------


API to retrieve Cloud Connectivity Gateway create options.

.. code:: python

    def get_cloud_connectivity_gateway_create_options(
        cloud_type: str,
        cloud_account_id: str,
        connectivity_gateway_type: Optional[
            ConnectivityGatewayTypeParam
        ] = None,
        refresh: Optional[str] = "false",
    ) -> InlineResponse20014: ...


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
        client.multicloud.interconnect.cloud.cloud_connectivity_gateways.create_options.get_cloud_connectivity_gateway_create_options()


.. toctree::
    :maxdepth: 1

    models

