===============
multicloud.site
===============


Operation: GET /dataservice/multicloud/site
-------------------------------------------


Get available sites

.. code:: python

    def get_sites(
        color: Optional[str] = None,
        attached: Optional[str] = None,
        solution: Optional[str] = None,
    ) -> GetSitesResponse: ...


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
        client.multicloud.site.get_sites()


.. toctree::
    :maxdepth: 1

    models

