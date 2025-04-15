==================================
stream.device.capture.forcedisbale
==================================


Operation: GET /dataservice/stream/device/capture/forcedisbale/{sessionId}
--------------------------------------------------------------------------


Force stop packet capture session

.. code:: python

    def get(session_id: str) -> ForceStopPacketCaptureRes: ...


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
        client.stream.device.capture.forcedisbale.get()


.. toctree::
    :maxdepth: 1

    models

