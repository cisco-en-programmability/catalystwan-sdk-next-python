===================================================
v1.feature_profile.sdwan.service.dhcp_server.schema
===================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/dhcp-server/schema
-------------------------------------------------------------------------------


Get a SDWAN Service DhcpServer Parcel Schema by Schema Type

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
        client.v1.feature_profile.sdwan.service.dhcp_server.schema.get()


.. toctree::
    :maxdepth: 1

    models

