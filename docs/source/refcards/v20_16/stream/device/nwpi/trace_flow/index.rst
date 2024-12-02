=============================
stream.device.nwpi.trace_flow
=============================


Operation: GET /dataservice/stream/device/nwpi/traceFlow
--------------------------------------------------------


Deprecated!!!

getTraceFlow

.. code:: python

    def get_trace_flow(
        trace_id: int, timestamp: int, state: str
    ) -> NwpitraceFlowRespPayload: ...


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
        client.stream.device.nwpi.trace_flow.get_trace_flow()


.. toctree::
    :maxdepth: 1

    models

