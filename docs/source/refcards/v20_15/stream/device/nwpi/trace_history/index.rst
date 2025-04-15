================================
stream.device.nwpi.trace_history
================================


Operation: GET /dataservice/stream/device/nwpi/traceHistory
-----------------------------------------------------------


Get historical traces

.. code:: python

    def get(
        trace_model: Optional[str] = None,
    ) -> NwpiTraceHistoryRespPayload: ...


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
        client.stream.device.nwpi.trace_history.get()


.. toctree::
    :maxdepth: 1

    models

