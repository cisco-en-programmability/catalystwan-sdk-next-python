==========================================
stream.device.nwpi.event_readout_by_traces
==========================================


Operation: GET /dataservice/stream/device/nwpi/eventReadoutByTraces
-------------------------------------------------------------------


Deprecated!!!

Get event Readout By Traces

.. code:: python

    def get_event_readout_by_traces(
        trace_id: List[int],
        entry_time: List[int],
        vpn: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> EventReadoutsResponsePayloadData: ...


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
        client.stream.device.nwpi.event_readout_by_traces.get_event_readout_by_traces()


.. toctree::
    :maxdepth: 1

    models

