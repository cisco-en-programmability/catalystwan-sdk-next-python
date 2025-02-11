=============================
stream.device.capture.disable
=============================


Operation: GET /dataservice/stream/device/capture/disable/{sessionId}
---------------------------------------------------------------------


Disable packet capture session

.. code:: python

    def disable_packet_capture_session(
        session_id: str,
    ) -> DisablePacketCaptureRes: ...


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
        client.stream.device.capture.disable.disable_packet_capture_session()


.. toctree::
    :maxdepth: 1

    models

