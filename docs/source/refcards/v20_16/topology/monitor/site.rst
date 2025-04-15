=====================
topology.monitor.site
=====================


Operation: GET /dataservice/topology/monitor/site/{siteId}
----------------------------------------------------------


Get topology monitor data for a given site id

.. code:: python

    def get(site_id: str) -> Any: ...


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
        client.topology.monitor.site.get()


