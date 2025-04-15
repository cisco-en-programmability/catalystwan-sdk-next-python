===============================
v1.topology_group.device.deploy
===============================


Operation: POST /dataservice/v1/topology-group/{topologyGroupId}/device/deploy
------------------------------------------------------------------------------


deploy Topology group to devices

.. code:: python

    def post(
        topology_group_id: str, payload: DeployTopologyGroupPostRequest
    ) -> DeployTopologyGroupPostResponse: ...


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
        client.v1.topology_group.device.deploy.post()


.. toctree::
    :maxdepth: 1

    models

