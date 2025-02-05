===============================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.schema
===============================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/wan/vpn/interface/gre/schema
-------------------------------------------------------------------------------------------


Get a Cedge Transport WanVpn InterfaceGre Schema by Schema Type

.. code:: python

    def get_cedge_transport_wan_vpn_interface_gre_parcel_schema_by_schema(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.schema.get_cedge_transport_wan_vpn_interface_gre_parcel_schema_by_schema()


.. toctree::
    :maxdepth: 1

    models

