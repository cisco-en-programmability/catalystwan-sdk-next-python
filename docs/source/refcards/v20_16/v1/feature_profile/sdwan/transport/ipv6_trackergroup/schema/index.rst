===========================================================
v1.feature_profile.sdwan.transport.ipv6_trackergroup.schema
===========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/ipv6-trackergroup/schema
---------------------------------------------------------------------------------------


Get a Cedge Transport IPv6 TrackerGroup Parcel Schema by Schema Type

.. code:: python

    def get_cedge_transport_ipv6_tracker_group_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.schema.get_cedge_transport_ipv6_tracker_group_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

