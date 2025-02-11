=========================
multicloud.imagename.edge
=========================


Operation: GET /dataservice/multicloud/imagename/edge
-----------------------------------------------------


Deprecated!!!

Get Edge provider supported images

.. code:: python

    def get_supported_edge_image_names(
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
        client.multicloud.imagename.edge.get_supported_edge_image_names()


.. toctree::
    :maxdepth: 1

    models

