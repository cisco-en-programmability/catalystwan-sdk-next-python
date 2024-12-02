=============================
stream.device.nwpi.trace.stop
=============================


Operation: POST /dataservice/stream/device/nwpi/trace/stop/{traceId}
--------------------------------------------------------------------


Trace Action - Stop

.. code:: python

    def trace_stop(trace_id: str) -> NwpiTraceStopRespPayload: ...


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
        client.stream.device.nwpi.trace.stop.trace_stop()


.. toctree::
    :maxdepth: 1

    models

