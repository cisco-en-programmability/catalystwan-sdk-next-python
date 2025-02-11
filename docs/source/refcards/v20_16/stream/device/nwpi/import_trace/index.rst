===============================
stream.device.nwpi.import_trace
===============================


Operation: POST /dataservice/stream/device/nwpi/importTrace
-----------------------------------------------------------


Import Trace

.. code:: python

    def import_trace(
        payload: Optional[ImportTraceRequest] = None,
        new_trace_name: Optional[str] = None,
    ) -> ImportTraceResponse: ...


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
        client.stream.device.nwpi.import_trace.import_trace()


.. toctree::
    :maxdepth: 1

    models

