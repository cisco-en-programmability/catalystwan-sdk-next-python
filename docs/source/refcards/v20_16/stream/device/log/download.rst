==========================
stream.device.log.download
==========================


Operation: GET /dataservice/stream/device/log/download/{sessionId}
------------------------------------------------------------------


.. code:: python

    def get(session_id: str) -> None: ...


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
        client.stream.device.log.download.get()


