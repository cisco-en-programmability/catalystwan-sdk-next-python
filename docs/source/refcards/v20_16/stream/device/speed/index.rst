===================
stream.device.speed
===================


Operation: POST /dataservice/stream/device/speed
------------------------------------------------


.. code:: python

    def get_session(payload: SpeedTestSession) -> SpeedTestResponse: ...


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
        client.stream.device.speed.get_session()


Operation: POST /dataservice/stream/device/speed/{deviceUUID}/{sessionId}
-------------------------------------------------------------------------


.. code:: python

    def save_speed_test_results(
        device_uuid: str,
        session_id: Uuid,
        payload: Optional[SpeedTestResult] = None,
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
        client.stream.device.speed.save_speed_test_results()


Operation: GET /dataservice/stream/device/speed/{sessionId}
-----------------------------------------------------------


.. code:: python

    def get_speed_test(
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
        client.stream.device.speed.get_speed_test()


.. toctree::
    :maxdepth: 1

    disable/index
    interface/index
    start/index
    status/index
    stop/index
    models

