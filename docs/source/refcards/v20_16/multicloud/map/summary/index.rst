======================
multicloud.map.summary
======================


Operation: GET /dataservice/multicloud/map/summary
--------------------------------------------------


Get mapping summary

.. code:: python

    def get(
        cloud_type: Optional[CloudTypeParam] = None,
        vpn_tunnel_status: Optional[str] = None,
    ) -> List[MapSummary]: ...


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
        client.multicloud.map.summary.get()


.. toctree::
    :maxdepth: 1

    models

