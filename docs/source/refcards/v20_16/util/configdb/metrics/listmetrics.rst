=================================
util.configdb.metrics.listmetrics
=================================


Operation: GET /dataservice/util/configdb/metrics/listmetrics
-------------------------------------------------------------


Fetches the list of enabled metrics

.. code:: python

    def get_metrics_list() -> Any: ...


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
        client.util.configdb.metrics.listmetrics.get_metrics_list()


