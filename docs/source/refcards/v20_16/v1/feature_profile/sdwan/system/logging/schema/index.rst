==============================================
v1.feature_profile.sdwan.system.logging.schema
==============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/logging/schema
--------------------------------------------------------------------------


Get a SDWAN System Logging Parcel Schema by Schema Type

.. code:: python

    def get_sdwan_system_logging_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.system.logging.schema.get_sdwan_system_logging_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

