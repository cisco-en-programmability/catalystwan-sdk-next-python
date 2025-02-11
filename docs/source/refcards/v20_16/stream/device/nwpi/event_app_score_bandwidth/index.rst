============================================
stream.device.nwpi.event_app_score_bandwidth
============================================


Operation: GET /dataservice/stream/device/nwpi/eventAppScoreBandwidth
---------------------------------------------------------------------


Deprecated!!!

Get Trace Event Application Performance Score and Bandwidth for NWPI.

.. code:: python

    def get_event_app_score_bandwidth(
        trace_id: int,
        timestamp: int,
        received_timestamp: int,
        state: Optional[str] = None,
        server_side_key: Optional[str] = None,
        client_side_key: Optional[str] = None,
        version: Optional[str] = None,
        vpn: Optional[str] = None,
    ) -> List[EventAppScoreBandwidthResponsePayloadInner]: ...


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
        client.stream.device.nwpi.event_app_score_bandwidth.get_event_app_score_bandwidth()


.. toctree::
    :maxdepth: 1

    models

