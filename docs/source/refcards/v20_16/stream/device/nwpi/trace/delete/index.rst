===============================
stream.device.nwpi.trace.delete
===============================


Operation: DELETE /dataservice/stream/device/nwpi/trace/delete
--------------------------------------------------------------


Trace Action - Delete

.. code:: python

    def delete(
        trace_id: str, timestamp: int
    ) -> NwpiTraceDeleteRespPayload: ...


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
        client.stream.device.nwpi.trace.delete.delete()


.. toctree::
    :maxdepth: 1

    models

