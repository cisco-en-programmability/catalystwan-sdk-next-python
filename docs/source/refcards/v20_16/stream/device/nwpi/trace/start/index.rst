==============================
stream.device.nwpi.trace.start
==============================


Operation: POST /dataservice/stream/device/nwpi/trace/start
-----------------------------------------------------------


Trace Action - Start

.. code:: python

    def post(
        payload: NwpiTraceStartReqPayload,
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
        client.stream.device.nwpi.trace.start.post()


.. toctree::
    :maxdepth: 1

    models

