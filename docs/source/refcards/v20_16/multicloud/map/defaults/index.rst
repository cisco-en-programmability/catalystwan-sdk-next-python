=======================
multicloud.map.defaults
=======================


Operation: GET /dataservice/multicloud/map/defaults
---------------------------------------------------


Get default mapping values

.. code:: python

    def get(cloud_type: CloudTypeParam) -> List[MapDefaults]: ...


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
        client.multicloud.map.defaults.get()


.. toctree::
    :maxdepth: 1

    models

