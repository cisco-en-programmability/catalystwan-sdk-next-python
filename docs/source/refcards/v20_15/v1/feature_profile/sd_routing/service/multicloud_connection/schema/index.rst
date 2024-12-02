==================================================================
v1.feature_profile.sd_routing.service.multicloud_connection.schema
==================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/multicloud-connection/schema
----------------------------------------------------------------------------------------------


Get Multicloud Connection Parcel Schema by Schema Type

.. code:: python

    def get_sd_routing_service_multicloud_connection_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.schema.get_sd_routing_service_multicloud_connection_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

