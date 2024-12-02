===========================================================================
v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.schema
===========================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/management/vpn/interface/ethernet/schema
-------------------------------------------------------------------------------------------------------


Get a SDWAN Transport ManagementVpn InterfaceEthernet Schema by Schema Type

.. code:: python

    def get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.schema.get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema()


.. toctree::
    :maxdepth: 1

    models

