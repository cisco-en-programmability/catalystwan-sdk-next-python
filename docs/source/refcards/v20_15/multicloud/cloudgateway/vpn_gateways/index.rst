====================================
multicloud.cloudgateway.vpn_gateways
====================================


Operation: GET /dataservice/multicloud/cloudgateway/vpn-gateways
----------------------------------------------------------------


Discover Azure Vpn Gateways

.. code:: python

    def get_azure_vpn_gateways(
        cloud_type: str,
        account_id: str,
        region: str,
        resource_group_name: str,
        resource_group_source: str,
        vhub_name: str,
        vhub_source: str,
    ) -> List[VpnGatewayResponse]: ...


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
        client.multicloud.cloudgateway.vpn_gateways.get_azure_vpn_gateways()


.. toctree::
    :maxdepth: 1

    models

