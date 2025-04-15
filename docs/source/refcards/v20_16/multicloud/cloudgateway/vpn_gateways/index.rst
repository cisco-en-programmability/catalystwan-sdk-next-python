====================================
multicloud.cloudgateway.vpn_gateways
====================================


Operation: GET /dataservice/multicloud/cloudgateway/vpn-gateways
----------------------------------------------------------------


Discover Azure Vpn Gateways

.. code:: python

    def get(
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
        client.multicloud.cloudgateway.vpn_gateways.get()


.. toctree::
    :maxdepth: 1

    models

