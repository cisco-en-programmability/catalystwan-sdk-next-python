===========================
stream.device.nwpi.agg_flow
===========================


Operation: GET /dataservice/stream/device/nwpi/aggFlow
------------------------------------------------------


Deprecated!!!

Get aggregated flow data for NWPI.

.. code:: python

    def get_agg_flow(
        trace_id: int,
        timestamp: int,
        trace_state: str,
        query: Optional[str] = None,
    ) -> List[AggFlowResponsePayloadInner]: ...


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
        client.stream.device.nwpi.agg_flow.get_agg_flow()


.. toctree::
    :maxdepth: 1

    models

