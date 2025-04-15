======================================
statistics.eiolte.cellular_aggregation
======================================


Operation: POST /dataservice/statistics/eiolte/cellularAggregation
------------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def post(payload: StatisticsDbQueryParam) -> Any: ...


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
        client.statistics.eiolte.cellular_aggregation.post()


.. toctree::
    :maxdepth: 1

    models

