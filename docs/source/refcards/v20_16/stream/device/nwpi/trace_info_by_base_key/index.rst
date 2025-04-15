=========================================
stream.device.nwpi.trace_info_by_base_key
=========================================


Operation: GET /dataservice/stream/device/nwpi/traceInfoByBaseKey
-----------------------------------------------------------------


Deprecated!!!

Get TraceInfoByBaseKey

.. code:: python

    def get(
        trace_id: int, entry_time: int, trace_model: Optional[str] = None
    ) -> TraceInfoResponsePayload: ...


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
        client.stream.device.nwpi.trace_info_by_base_key.get()


.. toctree::
    :maxdepth: 1

    models

