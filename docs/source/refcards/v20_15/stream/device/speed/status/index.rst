==========================
stream.device.speed.status
==========================


Operation: GET /dataservice/stream/device/speed/status/{sessionId}
------------------------------------------------------------------


.. code:: python

    def get_speed_test_status(
        session_id: Uuid,
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
        client.stream.device.speed.status.get_speed_test_status()


.. toctree::
    :maxdepth: 1

    models

