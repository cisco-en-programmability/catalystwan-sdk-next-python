================================
stream.device.log.sessions.clear
================================


Operation: GET /dataservice/stream/device/log/sessions/clear/{sessionId}
------------------------------------------------------------------------


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
        client.stream.device.log.sessions.clear.get()


