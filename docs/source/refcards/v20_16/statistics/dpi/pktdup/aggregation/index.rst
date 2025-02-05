=================================
statistics.dpi.pktdup.aggregation
=================================


Operation: POST /dataservice/statistics/dpi/pktdup/aggregation
--------------------------------------------------------------


Get time series aggregation data for packet duplication for an application over TLOCs if available

.. code:: python

    def get_dpi_stats_aggregation_data_for_packet_dup(
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
        client.statistics.dpi.pktdup.aggregation.get_dpi_stats_aggregation_data_for_packet_dup()


.. toctree::
    :maxdepth: 1

    models

