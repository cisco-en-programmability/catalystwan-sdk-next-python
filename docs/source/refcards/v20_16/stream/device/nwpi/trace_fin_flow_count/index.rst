=======================================
stream.device.nwpi.trace_fin_flow_count
=======================================


Operation: GET /dataservice/stream/device/nwpi/traceFinFlowCount
----------------------------------------------------------------


Deprecated!!!

Retrieve total Fin Flow counts

.. code:: python

    def get_finalized_flow_count(
        trace_id: int, timestamp: int
    ) -> InlineResponse200: ...


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
        client.stream.device.nwpi.trace_fin_flow_count.get_finalized_flow_count()


.. toctree::
    :maxdepth: 1

    models

