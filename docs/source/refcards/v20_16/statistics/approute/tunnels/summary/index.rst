===================================
statistics.approute.tunnels.summary
===================================


Operation: GET /dataservice/statistics/approute/tunnels/summary/{type}
----------------------------------------------------------------------


Get tunnel top statistics from device

.. code:: python

    def get(
        type_: str,
        query: Optional[str] = None,
        limit: Optional[int] = 10,
        site_id: Optional[str] = None,
    ) -> AppRouteTransportResp: ...


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
        client.statistics.approute.tunnels.summary.get()


.. toctree::
    :maxdepth: 1

    models

