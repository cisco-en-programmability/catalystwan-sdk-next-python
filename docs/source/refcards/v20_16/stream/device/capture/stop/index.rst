==========================
stream.device.capture.stop
==========================


Operation: GET /dataservice/stream/device/capture/stop/{sessionId}
------------------------------------------------------------------


Stop packet capture session

.. code:: python

    def get(session_id: str) -> PacketCaptureInfo: ...


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
        client.stream.device.capture.stop.get()


.. toctree::
    :maxdepth: 1

    models

