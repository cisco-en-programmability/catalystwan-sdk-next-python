=====================
util.configdb.metrics
=====================


Operation: GET /dataservice/util/configdb/metrics
-------------------------------------------------


By passing in the appropriate metric, it will return the values of  the respective metric within the timeframe provided

.. code:: python

    def return_metric(
        metric_name: str,
        start_date: str,
        end_date: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        page_no: Optional[int] = 1,
        limit: Optional[int] = 500,
    ) -> Neo4JMetricsResponse: ...


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
        client.util.configdb.metrics.return_metric()


.. toctree::
    :maxdepth: 1

    downloadfiles
    listmetrics
    models

