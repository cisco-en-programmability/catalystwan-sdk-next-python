==================================
stream.device.nwpi.packet_features
==================================


Operation: GET /dataservice/stream/device/nwpi/packetFeatures
-------------------------------------------------------------


Deprecated!!!

packetFeatures for NWPI.

.. code:: python

    def get(
        trace_id: int, timestamp: int, flow_id: int
    ) -> NwpipacketRespPayload: ...


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
        client.stream.device.nwpi.packet_features.get()


.. toctree::
    :maxdepth: 1

    models

