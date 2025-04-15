============================================
stream.device.nwpi.trace_fin_flow_time_range
============================================


Operation: GET /dataservice/stream/device/nwpi/traceFinFlowTimeRange
--------------------------------------------------------------------


Deprecated!!!

Retrieve Fin Flow time range

.. code:: python

    def get(
        trace_id: int, timestamp: int, state: str
    ) -> List[TraceFinFlowTimeRangeResponsePayloadInner]: ...


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
        client.stream.device.nwpi.trace_fin_flow_time_range.get()


.. toctree::
    :maxdepth: 1

    models

