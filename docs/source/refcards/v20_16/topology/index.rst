========
topology
========


Operation: GET /dataservice/topology
------------------------------------


Create full topology

.. code:: python

    def create_full_topology() -> List[Any]: ...


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
        client.topology.create_full_topology()


.. toctree::
    :maxdepth: 1

    device/index
    monitor/index
    physical/index

