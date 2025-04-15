=====================================
stream.device.nwpi.event_app_hop_list
=====================================


Operation: GET /dataservice/stream/device/nwpi/eventAppHopList
--------------------------------------------------------------


Deprecated!!!

Get Trace Application and HopList for NWPI.

.. code:: python

    def get(
        trace_id: int,
        timestamp: int,
        state: Optional[str] = None,
        version: Optional[str] = None,
        server_side_key: Optional[str] = None,
        client_side_key: Optional[str] = None,
        vpn: Optional[str] = None,
    ) -> List[EventAppHopListResponsePayloadInner]: ...


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
        client.stream.device.nwpi.event_app_hop_list.get()


.. toctree::
    :maxdepth: 1

    models

