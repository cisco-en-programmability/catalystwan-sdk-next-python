==================
multicloud.regions
==================


Operation: GET /dataservice/multicloud/regions
----------------------------------------------


Obtain all supported Cloud Service Provider (CSP) types

.. code:: python

    def get_cloud_regions(
        cloud_type: Optional[CloudTypeParam] = None,
    ) -> List[GetRegions]: ...


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
        client.multicloud.regions.get_cloud_regions()


.. toctree::
    :maxdepth: 1

    models

