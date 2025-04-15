=======================================
stream.device.nwpi.trace_readout_filter
=======================================


Operation: GET /dataservice/stream/device/nwpi/traceReadoutFilter
-----------------------------------------------------------------


Deprecated!!!

Get event Readout Filter By Traces

.. code:: python

    def get(
        trace_id: List[int], entry_time: List[int]
    ) -> EventReadoutFilterResponsePayload: ...


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
        client.stream.device.nwpi.trace_readout_filter.get()


.. toctree::
    :maxdepth: 1

    models

