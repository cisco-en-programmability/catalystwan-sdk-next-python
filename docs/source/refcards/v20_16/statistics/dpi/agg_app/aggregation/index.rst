==================================
statistics.dpi.agg_app.aggregation
==================================


Operation: POST /dataservice/statistics/dpi/agg-app/aggregation
---------------------------------------------------------------


Get raw aggregated data and display applications with the highest utilization for a device

.. code:: python

    def get_agg_app_data_post(
        payload: Optional[Any] = None, site_id: Optional[str] = None
    ) -> DpiAggregationResponse: ...


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
        client.statistics.dpi.agg_app.aggregation.get_agg_app_data_post()


.. toctree::
    :maxdepth: 1

    models

