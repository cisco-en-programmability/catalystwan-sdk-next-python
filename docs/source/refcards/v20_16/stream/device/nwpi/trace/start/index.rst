==============================
stream.device.nwpi.trace.start
==============================


Operation: POST /dataservice/stream/device/nwpi/trace/start
-----------------------------------------------------------


Trace Action - Start

.. code:: python

    def trace_start(
        payload: Optional[NwpiTraceStartReqPayload] = None,
    ) -> NwpiTraceStartRespPayload: ...


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
        client.stream.device.nwpi.trace.start.trace_start()


.. toctree::
    :maxdepth: 1

    models

