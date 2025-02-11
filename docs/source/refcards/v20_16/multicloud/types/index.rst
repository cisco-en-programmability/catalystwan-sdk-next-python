================
multicloud.types
================


Operation: GET /dataservice/multicloud/types
--------------------------------------------


Obtain all supported Cloud Service Provider (CSP) types

.. code:: python

    def get_cloud_types() -> Any: ...


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
        client.multicloud.types.get_cloud_types()


.. toctree::
    :maxdepth: 1

    edge

