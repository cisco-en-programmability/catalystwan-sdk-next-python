===================================
statistics.dpi.recovery.aggregation
===================================


Operation: POST /dataservice/statistics/dpi/recovery/aggregation
----------------------------------------------------------------


Get aggregation data and fec recovery rate if available

.. code:: python

    def post(payload: Any) -> FecAndPktDupResponse: ...


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
        client.statistics.dpi.recovery.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

