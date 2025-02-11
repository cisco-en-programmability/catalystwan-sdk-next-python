====================================
statistics.eiolte.unique_aggregation
====================================


Operation: POST /dataservice/statistics/eiolte/uniqueAggregation
----------------------------------------------------------------


Get unique aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def unique_aggregation(
        payload: Optional[StatisticsDbQueryParam] = None,
    ) -> Any: ...


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
        client.statistics.eiolte.unique_aggregation.unique_aggregation()


.. toctree::
    :maxdepth: 1

    models

