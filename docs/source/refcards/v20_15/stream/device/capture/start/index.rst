===========================
stream.device.capture.start
===========================


Operation: GET /dataservice/stream/device/capture/start/{sessionId}
-------------------------------------------------------------------


Start packet capture session

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
        client.stream.device.capture.start.get()


.. toctree::
    :maxdepth: 1

    models

