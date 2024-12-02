===================================
statistics.approute.fec.aggregation
===================================


Operation: POST /dataservice/statistics/approute/fec/aggregation
----------------------------------------------------------------


Get aggregation data and fec recovery rate

.. code:: python

    def get_app_route_fec_agg(
        payload: Optional[Any] = None, site_id: Optional[str] = None
    ) -> List[AppRouteFecAggRespInner]: ...


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
        client.statistics.approute.fec.aggregation.get_app_route_fec_agg()


.. toctree::
    :maxdepth: 1

    models

