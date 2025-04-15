====================================
multicloud.locations.edge.account_id
====================================


Operation: PUT /dataservice/multicloud/locations/edge/{edgeType}/accountId/{accountId}
--------------------------------------------------------------------------------------


Deprecated!!!

Update Edge Locations

.. code:: python

    def put(edge_type: EdgeTypeParam, account_id: str) -> Any: ...


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
        client.multicloud.locations.edge.account_id.put()


.. toctree::
    :maxdepth: 1

    models

