==========================================================
v1.feature_profile.sdwan.transport.t1_e1_controller.schema
==========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/t1-e1-controller/schema
--------------------------------------------------------------------------------------


Get a Cedge Transport T1e1controller Parcel Schema by Schema Type

.. code:: python

    def get_cedge_transport_t1e1controller_parcel_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.schema.get_cedge_transport_t1e1controller_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

