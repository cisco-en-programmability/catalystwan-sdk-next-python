=========================================
stream.device.nwpi.active_flow_with_query
=========================================


Operation: GET /dataservice/stream/device/nwpi/activeFlowWithQuery
------------------------------------------------------------------


Deprecated!!!

Get active flows for NWPI.

.. code:: python

    def active_flow_with_query(
        trace_id: int, timestamp: int, query: Optional[str] = None
    ) -> ActiveFlowResponsePayload: ...


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
        client.stream.device.nwpi.active_flow_with_query.active_flow_with_query()


.. toctree::
    :maxdepth: 1

    models

