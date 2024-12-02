==========================
statistics.dpi.aggregation
==========================


Operation: GET /dataservice/statistics/dpi/aggregation
------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_dpi_stats_aggregation_data(
        query: Optional[str] = None,
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
        client.statistics.dpi.aggregation.get_dpi_stats_aggregation_data()


Operation: POST /dataservice/statistics/dpi/aggregation
-------------------------------------------------------


Get raw aggregated data and display applications with the highest utilization for a device

.. code:: python

    def get_dpi_stats_aggregation_data_post(
        payload: Optional[Any] = None,
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
        client.statistics.dpi.aggregation.get_dpi_stats_aggregation_data_post()


.. toctree::
    :maxdepth: 1

    models

