=================================
statistics.dpi.pktdup.aggregation
=================================


Operation: POST /dataservice/statistics/dpi/pktdup/aggregation
--------------------------------------------------------------


Get time series aggregation data for packet duplication for an application over TLOCs if available

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
        client.statistics.dpi.pktdup.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

