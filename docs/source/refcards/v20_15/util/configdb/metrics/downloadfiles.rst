===================================
util.configdb.metrics.downloadfiles
===================================


Operation: GET /dataservice/util/configdb/metrics/downloadfiles
---------------------------------------------------------------


By passing in the appropriate metric, date, start and end time, it will return a tar file consisting of all the metric files of the respective metric within the timeframe provided

.. code:: python

    def get(
        metric_name: str,
        start_date: str,
        end_date: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
    ) -> str: ...


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
        client.util.configdb.metrics.downloadfiles.get()


