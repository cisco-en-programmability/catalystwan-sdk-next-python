====================================================
v1.feature_profile.sdwan.service.trackergroup.schema
====================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/trackergroup/schema
--------------------------------------------------------------------------------


Get a Cedge Service TrackerGroup Parcel Schema by Schema Type

.. code:: python

    def get_cedge_service_tracker_group_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.service.trackergroup.schema.get_cedge_service_tracker_group_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

