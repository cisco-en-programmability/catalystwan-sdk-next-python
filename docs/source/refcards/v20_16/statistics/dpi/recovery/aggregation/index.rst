===================================
statistics.dpi.recovery.aggregation
===================================


Operation: POST /dataservice/statistics/dpi/recovery/aggregation
----------------------------------------------------------------


Get aggregation data and fec recovery rate if available

.. code:: python

    def get_dpi_stats_aggregation_data_for_fec(
        payload: Optional[Any] = None,
    ) -> FecAndPktDupResponse: ...


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
        client.statistics.dpi.recovery.aggregation.get_dpi_stats_aggregation_data_for_fec()


.. toctree::
    :maxdepth: 1

    models

