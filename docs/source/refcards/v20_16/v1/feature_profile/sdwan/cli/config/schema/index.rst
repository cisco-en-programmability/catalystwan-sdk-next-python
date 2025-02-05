==========================================
v1.feature_profile.sdwan.cli.config.schema
==========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/config/schema
----------------------------------------------------------------------


Get a Sdwan Cli Config feature Schema by Schema Type

.. code:: python

    def get_sdwan_cli_config_feature_schema_by_schema_type(
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
        client.v1.feature_profile.sdwan.cli.config.schema.get_sdwan_cli_config_feature_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

