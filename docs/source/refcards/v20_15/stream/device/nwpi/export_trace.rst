===============================
stream.device.nwpi.export_trace
===============================


Operation: GET /dataservice/stream/device/nwpi/exportTrace
----------------------------------------------------------


Export NWPI Trace Data

.. code:: python

    def export_trace(trace_id: int, timestamp: int) -> Any: ...


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
        client.stream.device.nwpi.export_trace.export_trace()


