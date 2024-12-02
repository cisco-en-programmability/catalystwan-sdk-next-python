============================
multicloud.instancesize.edge
============================


Operation: GET /dataservice/multicloud/instancesize/edge
--------------------------------------------------------


Deprecated!!!

Get Edge provider supported size

.. code:: python

    def get_supported_edge_instance_size(
        edge_type: Optional[EdgeTypeParam] = "MEGAPORT",
    ) -> Any: ...


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
        client.multicloud.instancesize.edge.get_supported_edge_instance_size()


.. toctree::
    :maxdepth: 1

    models

