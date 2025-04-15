======================
multicloud.edge.device
======================


Operation: GET /dataservice/multicloud/edge/{edgeType}/device
-------------------------------------------------------------


Deprecated!!!

Get available WAN edge devices

.. code:: python

    def get(edge_type: EdgeTypeParam) -> Any: ...


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
        client.multicloud.edge.device.get()


.. toctree::
    :maxdepth: 1

    models

