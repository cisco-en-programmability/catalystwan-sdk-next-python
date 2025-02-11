=================================
stream.device.nwpi.finalized_data
=================================


Operation: GET /dataservice/stream/device/nwpi/finalizedData
------------------------------------------------------------


Deprecated!!!

finalizedData for NWPI.

.. code:: python

    def get_finalized_data(
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
        client.stream.device.nwpi.finalized_data.get_finalized_data()


.. toctree::
    :maxdepth: 1

    models

