============================================
stream.device.nwpi.trace_fin_flow_with_query
============================================


Operation: GET /dataservice/stream/device/nwpi/traceFinFlowWithQuery
--------------------------------------------------------------------


Deprecated!!!

Retrieve Certain Fin Flows

.. code:: python

    def get(
        trace_id: int, timestamp: int, query: Optional[str] = None
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
        client.stream.device.nwpi.trace_fin_flow_with_query.get()


.. toctree::
    :maxdepth: 1

    models

