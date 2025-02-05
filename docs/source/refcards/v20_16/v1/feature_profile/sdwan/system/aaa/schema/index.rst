==========================================
v1.feature_profile.sdwan.system.aaa.schema
==========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/aaa/schema
----------------------------------------------------------------------


Get a SDWAN System Aaa Parcel Schema by Schema Type

.. code:: python

    def get_sdwan_system_aaa_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.system.aaa.schema.get_sdwan_system_aaa_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

