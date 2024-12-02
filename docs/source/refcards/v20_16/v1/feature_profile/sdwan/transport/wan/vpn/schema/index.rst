=================================================
v1.feature_profile.sdwan.transport.wan.vpn.schema
=================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/wan/vpn/schema
-----------------------------------------------------------------------------


Get a SDWAN Transport WanVpn Parcel Schema by Schema Type

.. code:: python

    def get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.schema.get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

