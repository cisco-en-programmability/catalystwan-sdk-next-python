===================
multicloud.map.vpns
===================


Operation: GET /dataservice/multicloud/map/vpns
-----------------------------------------------


Get default mapping values

.. code:: python

    def get_mapping_vpns() -> MapVpnsResponse: ...


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
        client.multicloud.map.vpns.get_mapping_vpns()


.. toctree::
    :maxdepth: 1

    models

