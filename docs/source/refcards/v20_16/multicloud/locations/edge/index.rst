=========================
multicloud.locations.edge
=========================


Operation: GET /dataservice/multicloud/locations/edge/{edgeType}
----------------------------------------------------------------


Deprecated!!!

Get Edge Locations

.. code:: python

    def get(
        edge_type: EdgeTypeParam,
        account_id: Optional[str] = None,
        region: Optional[str] = None,
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
        client.multicloud.locations.edge.get()


Operation: DELETE /dataservice/multicloud/locations/edge/{edgeType}
-------------------------------------------------------------------


Deprecated!!!

Delete edge account

.. code:: python

    def delete(edge_type: EdgeTypeParam) -> None: ...


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
        client.multicloud.locations.edge.delete()


.. toctree::
    :maxdepth: 1

    account_id/index
    models

