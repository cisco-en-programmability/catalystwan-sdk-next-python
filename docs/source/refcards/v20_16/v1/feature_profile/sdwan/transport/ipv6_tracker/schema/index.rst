======================================================
v1.feature_profile.sdwan.transport.ipv6_tracker.schema
======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/ipv6-tracker/schema
----------------------------------------------------------------------------------


Get a SDWAN Transport IPv6 Tracker Parcel Schema by Schema Type

.. code:: python

    def get_sdwan_transport_ipv6_tracker_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.schema.get_sdwan_transport_ipv6_tracker_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

