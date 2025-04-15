===================
multicloud.map.tags
===================


Operation: GET /dataservice/multicloud/map/tags
-----------------------------------------------


Get cloud gateway types for specified cloudType

.. code:: python

    def get(
        cloud_type: Optional[CloudTypeParam] = None,
    ) -> TagsResponse: ...


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
        client.multicloud.map.tags.get()


.. toctree::
    :maxdepth: 1

    edge/index
    models

