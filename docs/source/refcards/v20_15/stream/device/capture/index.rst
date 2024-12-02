=====================
stream.device.capture
=====================


Operation: POST /dataservice/stream/device/capture
--------------------------------------------------


Create packet capture session

.. code:: python

    def get_session_info_capture(
        payload: CreatePacketCaptureReq,
    ) -> PacketCaptureInfo: ...


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
        client.stream.device.capture.get_session_info_capture()


Operation: POST /dataservice/stream/device/capture/{deviceUUID}/{sessionId}
---------------------------------------------------------------------------


Form post packet capture

.. code:: python

    def form_post_packet_capture(
        device_uuid: str, session_id: str
    ) -> FormPacketCaptureRes: ...


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
        client.stream.device.capture.form_post_packet_capture()


.. toctree::
    :maxdepth: 1

    disable/index
    download
    forcedisbale/index
    start/index
    status/index
    stop/index
    vnics_info/index
    models

