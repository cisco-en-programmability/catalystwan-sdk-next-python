====================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.schema
====================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/wan/vpn/interface/cellular/schema
------------------------------------------------------------------------------------------------


Get a SDWAN Transport WanVpn CellularInterface Schema by Schema Type

.. code:: python

    def get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema(
        schema_type: SchemaTypeParam,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.schema.get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema()


.. toctree::
    :maxdepth: 1

    models

