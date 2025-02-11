=================
v1.topology_group
=================


Operation: GET /dataservice/v1/topology-group
---------------------------------------------


Get a Topology Group by Solution

.. code:: python

    def get_topology_group_by_solution(
        solution: Optional[str] = None,
    ) -> List[TopologyGroup]: ...


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
        client.v1.topology_group.get_topology_group_by_solution()


Operation: POST /dataservice/v1/topology-group
----------------------------------------------


Create a new Topology Group

.. code:: python

    def create_topology_group(payload: Optional[str] = None) -> str: ...


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
        client.v1.topology_group.create_topology_group()


Operation: GET /dataservice/v1/topology-group/{topologyGroupId}
---------------------------------------------------------------


Get a Topology Group by ID

.. code:: python

    def get_topology_group(topology_group_id: str) -> TopologyGroup: ...


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
        client.v1.topology_group.get_topology_group()


Operation: PUT /dataservice/v1/topology-group/{topologyGroupId}
---------------------------------------------------------------


Edit a Topology Group

.. code:: python

    def edit_topology_group(
        topology_group_id: str, payload: Optional[str] = None
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
        client.v1.topology_group.edit_topology_group()


Operation: DELETE /dataservice/v1/topology-group/{topologyGroupId}
------------------------------------------------------------------


Delete Topology Group

.. code:: python

    def delete_topology_group(topology_group_id: str) -> None: ...


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
        client.v1.topology_group.delete_topology_group()


.. toctree::
    :maxdepth: 1

    device/index
    models

