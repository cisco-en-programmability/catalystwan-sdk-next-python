========================
stream.device.log.search
========================


Operation: POST /dataservice/stream/device/log/search/{sessionId}
-----------------------------------------------------------------


.. code:: python

    def search_device_log(
        session_id: str, payload: Optional[str] = None
    ) -> None: ...


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
        client.stream.device.log.search.search_device_log()


