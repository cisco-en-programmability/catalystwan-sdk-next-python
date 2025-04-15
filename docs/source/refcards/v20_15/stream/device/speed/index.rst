===================
stream.device.speed
===================


Operation: GET /dataservice/stream/device/speed/{sessionId}
-----------------------------------------------------------


.. code:: python

    def get(
        session_id: Uuid, log_id: Optional[int] = 0
    ) -> SpeedTestResultResponse: ...


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
        client.stream.device.speed.get()


Operation: POST /dataservice/stream/device/speed
------------------------------------------------


.. code:: python

    @overload
    def post(payload: SpeedTestSession) -> SpeedTestResponse: ...


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
        client.stream.device.speed.post()


Operation: POST /dataservice/stream/device/speed/{deviceUUID}/{sessionId}
-------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        payload: SpeedTestResult, device_uuid: str, session_id: Uuid
    ) -> SpeedTestStatusResponse: ...


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
        client.stream.device.speed.post()


.. toctree::
    :maxdepth: 1

    disable/index
    interface/index
    start/index
    status/index
    stop/index
    models

