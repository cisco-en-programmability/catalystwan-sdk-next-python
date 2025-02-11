=============================================
multicloud.interconnect.gateways.config_group
=============================================


Operation: POST /dataservice/multicloud/interconnect/gateways/config-group
--------------------------------------------------------------------------


API to initiate a config group creation for an Interconnect gateway.

.. code:: python

    def create_interconnect_gateway_config_group(
        interconnect_type: InterconnectTypeParam,
        payload: Optional[GatewaysConfiggroupBody] = None,
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
        client.multicloud.interconnect.gateways.config_group.create_interconnect_gateway_config_group()


.. toctree::
    :maxdepth: 1

    models

