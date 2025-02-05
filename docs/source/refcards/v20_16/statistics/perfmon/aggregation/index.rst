==============================
statistics.perfmon.aggregation
==============================


Operation: POST /dataservice/statistics/perfmon/aggregation
-----------------------------------------------------------


Get one application one site line chart data

.. code:: python

    def get_post_aggregation_data_by_query_15(
        payload: Optional[str] = None,
    ) -> List[ApplicationSiteChartItem]: ...


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
        client.statistics.perfmon.aggregation.get_post_aggregation_data_by_query_15()


.. toctree::
    :maxdepth: 1

    models

