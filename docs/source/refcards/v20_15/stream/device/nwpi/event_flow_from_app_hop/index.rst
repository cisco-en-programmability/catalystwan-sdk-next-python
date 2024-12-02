==========================================
stream.device.nwpi.event_flow_from_app_hop
==========================================


Operation: GET /dataservice/stream/device/nwpi/eventFlowFromAppHop
------------------------------------------------------------------


Deprecated!!!

Get Trace Event Flow From Application And Hop for NWPI.

.. code:: python

    def get_event_flow_from_app_hop(
        trace_id: int,
        timestamp: int,
        direction: str,
        from_: str,
        to: str,
        device_trace_id: int,
        state: Optional[str] = None,
        application: Optional[str] = None,
        version: Optional[str] = None,
        server_side_key: Optional[str] = None,
        client_side_key: Optional[str] = None,
        vpn: Optional[str] = None,
    ) -> List[EventFlowFromAppHopResponsePayloadInner]: ...


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
        client.stream.device.nwpi.event_flow_from_app_hop.get_event_flow_from_app_hop()


.. toctree::
    :maxdepth: 1

    models

