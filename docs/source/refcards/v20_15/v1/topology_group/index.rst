=================
v1.topology_group
=================


Operation: POST /dataservice/v1/topology-group
----------------------------------------------


Create a new Topology Group

.. code:: python

    def post(payload: CreateTopologyGroupPostRequest) -> str: ...


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
        client.v1.topology_group.post()


Operation: PUT /dataservice/v1/topology-group/{topologyGroupId}
---------------------------------------------------------------


Edit a Topology Group

.. code:: python

    def put(
        topology_group_id: str, payload: EditTopologyGroupPutRequest
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
        client.v1.topology_group.put()


Operation: DELETE /dataservice/v1/topology-group/{topologyGroupId}
------------------------------------------------------------------


Delete Topology Group

.. code:: python

    def delete(topology_group_id: str) -> None: ...


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
        client.v1.topology_group.delete()


Operation: GET /dataservice/v1/topology-group
---------------------------------------------


.. code:: python

    @overload
    def get(solution: Optional[str] = None) -> List[TopologyGroup]: ...


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
        client.v1.topology_group.get()


Operation: GET /dataservice/v1/topology-group/{topologyGroupId}
---------------------------------------------------------------


.. code:: python

    @overload
    def get(topology_group_id: str) -> TopologyGroup: ...


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
        client.v1.topology_group.get()


.. toctree::
    :maxdepth: 1

    device/index
    models

