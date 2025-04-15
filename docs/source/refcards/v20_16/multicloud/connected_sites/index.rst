==========================
multicloud.connected_sites
==========================


Operation: GET /dataservice/multicloud/connected-sites/{cloudType}
------------------------------------------------------------------


Get sites with connectivity to the cloud by cloud type

.. code:: python

    def get(
        cloud_type: str, cloud_gateway_name: Optional[str] = None
    ) -> ConnectedSitesResponse: ...


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
        client.multicloud.connected_sites.get()


.. toctree::
    :maxdepth: 1

    edge
    models

