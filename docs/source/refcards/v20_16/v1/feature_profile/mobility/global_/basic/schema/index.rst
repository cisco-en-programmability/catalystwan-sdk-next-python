================================================
v1.feature_profile.mobility.global_.basic.schema
================================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/basic/schema
---------------------------------------------------------------------------


Get a Mobility Global Basic Parcel Schema by Schema Type

.. code:: python

    def get_mobility_global_basic_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.mobility.global_.basic.schema.get_mobility_global_basic_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

