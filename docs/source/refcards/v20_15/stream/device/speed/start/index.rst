=========================
stream.device.speed.start
=========================


Operation: GET /dataservice/stream/device/speed/start/{sessionId}
-----------------------------------------------------------------


.. code:: python

    def start_speed_test(session_id: Uuid) -> SpeedTestStatusResponse: ...


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
        client.stream.device.speed.start.start_speed_test()


.. toctree::
    :maxdepth: 1

    models

