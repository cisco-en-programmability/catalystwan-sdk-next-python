=====================
stream.device.capture
=====================


Operation: POST /dataservice/stream/device/capture
--------------------------------------------------


.. code:: python

    @overload
    def post(payload: CreatePacketCaptureReq) -> PacketCaptureInfo: ...


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
        client.stream.device.capture.post()


Operation: POST /dataservice/stream/device/capture/{deviceUUID}/{sessionId}
---------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
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
        client.stream.device.capture.post()


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

