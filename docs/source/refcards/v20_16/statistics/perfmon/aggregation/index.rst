==============================
statistics.perfmon.aggregation
==============================


Operation: POST /dataservice/statistics/perfmon/aggregation
-----------------------------------------------------------


Get one application one site line chart data

.. code:: python

    def post(payload: str) -> List[ApplicationSiteChartItem]: ...


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
        client.statistics.perfmon.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

