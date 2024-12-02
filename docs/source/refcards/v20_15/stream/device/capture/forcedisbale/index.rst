==================================
stream.device.capture.forcedisbale
==================================


Operation: GET /dataservice/stream/device/capture/forcedisbale/{sessionId}
--------------------------------------------------------------------------


Force stop packet capture session

.. code:: python

    def force_stop_pcap_session(
        session_id: str,
    ) -> ForceStopPacketCaptureRes: ...


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
        client.stream.device.capture.forcedisbale.force_stop_pcap_session()


.. toctree::
    :maxdepth: 1

    models

