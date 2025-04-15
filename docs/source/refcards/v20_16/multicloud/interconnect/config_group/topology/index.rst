=============================================
multicloud.interconnect.config_group.topology
=============================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/config-group/{config-group-id}/topology
---------------------------------------------------------------------------------------------------------------


API to retrieve current Multicloud Interconnect topology for the Config Group.

.. code:: python

    def get(
        interconnect_type: str, config_group_id: str
    ) -> InlineResponse20013: ...


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
        client.multicloud.interconnect.config_group.topology.get()


Operation: PUT /dataservice/multicloud/interconnect/{interconnect-type}/config-group/{config-group-id}/topology
---------------------------------------------------------------------------------------------------------------


API to update current Multicloud Interconnect topology for the Config Group.

.. code:: python

    def put(
        interconnect_type: str, config_group_id: str
    ) -> InlineResponse20013: ...


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
        client.multicloud.interconnect.config_group.topology.put()


.. toctree::
    :maxdepth: 1

    models

