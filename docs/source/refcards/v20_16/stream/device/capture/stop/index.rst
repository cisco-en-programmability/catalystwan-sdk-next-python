==========================
stream.device.capture.stop
==========================


Operation: GET /dataservice/stream/device/capture/stop/{sessionId}
------------------------------------------------------------------


Stop packet capture session

.. code:: python

    def stop_pcap_session(session_id: str) -> PacketCaptureInfo: ...


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
        client.stream.device.capture.stop.stop_pcap_session()


.. toctree::
    :maxdepth: 1

    models

