================================
multicloud.config_group.topology
================================


Operation: GET /dataservice/multicloud/{cloudType}/config-group/{config-group-id}/topology
------------------------------------------------------------------------------------------


API to retrieve current Multicloud MultiCloud topology for the Config Group.

.. code:: python

    def get(
        cloud_type: str, config_group_id: str
    ) -> InlineResponse200: ...


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
        client.multicloud.config_group.topology.get()


Operation: PUT /dataservice/multicloud/{cloudType}/config-group/{config-group-id}/topology
------------------------------------------------------------------------------------------


API to update current MultiCloud topology for the Config Group.

.. code:: python

    def put(
        cloud_type: str, config_group_id: str
    ) -> InlineResponse200: ...


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
        client.multicloud.config_group.topology.put()


.. toctree::
    :maxdepth: 1

    models

