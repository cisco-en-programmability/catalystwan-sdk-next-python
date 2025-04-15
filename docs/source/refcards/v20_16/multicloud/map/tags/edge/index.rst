========================
multicloud.map.tags.edge
========================


Operation: GET /dataservice/multicloud/map/tags/edge
----------------------------------------------------


Deprecated!!!

Get default Interconnect mapping tag values

.. code:: python

    def get(
        cloud_type: CloudTypeParam,
        account_id: Optional[str] = None,
        resource_group: Optional[str] = None,
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
        client.multicloud.map.tags.edge.get()


.. toctree::
    :maxdepth: 1

    models

