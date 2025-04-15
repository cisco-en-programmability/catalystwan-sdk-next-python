==================================
stream.device.nwpi.concurrent_data
==================================


Operation: GET /dataservice/stream/device/nwpi/concurrentData
-------------------------------------------------------------


Deprecated!!!

Get concurrent data for NWPI.

.. code:: python

    def get(
        trace_id: int, timestamp: int
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
        client.stream.device.nwpi.concurrent_data.get()


.. toctree::
    :maxdepth: 1

    models

