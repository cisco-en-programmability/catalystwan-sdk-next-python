=================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.schema
=================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/wan/vpn/interface/ipsec/schema
---------------------------------------------------------------------------------------------


Get a SDWAN Transport WanVpn InterfaceIpsec Schema by Schema Type

.. code:: python

    def get_sdwan_profile_parcel_schema_1(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.schema.get_sdwan_profile_parcel_schema_1()


.. toctree::
    :maxdepth: 1

    models

