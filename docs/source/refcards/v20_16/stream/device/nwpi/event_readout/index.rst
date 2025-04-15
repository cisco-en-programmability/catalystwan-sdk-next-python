================================
stream.device.nwpi.event_readout
================================


Operation: GET /dataservice/stream/device/nwpi/eventReadout
-----------------------------------------------------------


Deprecated!!!

Get Trace Event Readout for NWPI.

.. code:: python

    def get(
        trace_id: int,
        timestamp: int,
        state: Optional[str] = None,
        vpn: Optional[str] = None,
        user_name: Optional[str] = None,
        version: Optional[str] = None,
    ) -> List[EventReadoutResponsePayloadInner]: ...


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
        client.stream.device.nwpi.event_readout.get()


.. toctree::
    :maxdepth: 1

    models

