=======================================
statistics.approute.app_agg.aggregation
=======================================


Operation: POST /dataservice/statistics/approute/app-agg/aggregation
--------------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_app_data_by_query9(
        payload: Optional[Any] = None,
    ) -> List[AppRouteAppAggRespInner]: ...


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
        client.statistics.approute.app_agg.aggregation.get_post_aggregation_app_data_by_query9()


.. toctree::
    :maxdepth: 1

    models

