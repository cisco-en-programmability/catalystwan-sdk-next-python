========================
stream.device.speed.stop
========================


Operation: GET /dataservice/stream/device/speed/stop/{sessionId}
----------------------------------------------------------------


.. code:: python

    def get(session_id: Uuid) -> SpeedTestStatusResponse: ...


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
        client.stream.device.speed.stop.get()


.. toctree::
    :maxdepth: 1

    models

