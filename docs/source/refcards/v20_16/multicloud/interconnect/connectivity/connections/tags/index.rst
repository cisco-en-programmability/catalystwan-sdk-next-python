=====================================================
multicloud.interconnect.connectivity.connections.tags
=====================================================


Operation: GET /dataservice/multicloud/interconnect/connectivity/connections/tags
---------------------------------------------------------------------------------


API to retrieve configured Interconnect host VPC/VNET mapping tags.

.. code:: python

    def get_interconnect_mapping_tags(
        cloud_type: str,
        cloud_account_id: str,
        resource_group: Optional[str] = None,
    ) -> InlineResponse2002: ...


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
        client.multicloud.interconnect.connectivity.connections.tags.get_interconnect_mapping_tags()


.. toctree::
    :maxdepth: 1

    models

