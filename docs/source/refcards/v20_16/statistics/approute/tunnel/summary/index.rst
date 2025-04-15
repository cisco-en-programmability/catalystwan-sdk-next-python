==================================
statistics.approute.tunnel.summary
==================================


Operation: GET /dataservice/statistics/approute/tunnel/{type}/summary
---------------------------------------------------------------------


Get tunnel top statistics in as chart

.. code:: python

    def get(
        type_: str, query: Optional[str] = None
    ) -> List[AppRouteRespWithPageInfo]: ...


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
        client.statistics.approute.tunnel.summary.get()


.. toctree::
    :maxdepth: 1

    models

