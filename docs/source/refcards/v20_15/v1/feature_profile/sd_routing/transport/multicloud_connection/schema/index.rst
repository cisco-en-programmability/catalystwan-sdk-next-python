====================================================================
v1.feature_profile.sd_routing.transport.multicloud_connection.schema
====================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/multicloud-connection/schema
------------------------------------------------------------------------------------------------


Get a SD-Routing tranport multicloud connection Schema by Schema Type

.. code:: python

    def get_sd_routing_transport_multicloud_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.schema.get_sd_routing_transport_multicloud_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

