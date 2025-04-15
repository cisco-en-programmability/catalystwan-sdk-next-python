=============================================
v1.feature_profile.sdwan.system.banner.schema
=============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/banner/schema
-------------------------------------------------------------------------


Get a SDWAN System Banner Parcel Schema by Schema Type

.. code:: python

    def get(schema_type: SchemaTypeParam) -> str: ...


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
        client.v1.feature_profile.sdwan.system.banner.schema.get()


.. toctree::
    :maxdepth: 1

    models

