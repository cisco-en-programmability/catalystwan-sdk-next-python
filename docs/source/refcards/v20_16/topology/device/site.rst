====================
topology.device.site
====================


Operation: GET /dataservice/topology/device/site/{siteId}
---------------------------------------------------------


Get topology for a given site id

.. code:: python

    def get_site_topology(site_id: str) -> Any: ...


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
        client.topology.device.site.get_site_topology()


