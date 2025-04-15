=================
stream.device.log
=================


Operation: GET /dataservice/stream/device/log/{sessionId}
---------------------------------------------------------


.. code:: python

    def get(session_id: Uuid, log_id: Optional[int] = -1) -> None: ...


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
        client.stream.device.log.get()


Operation: POST /dataservice/stream/device/log
----------------------------------------------


.. code:: python

    @overload
    def post(payload: str) -> None: ...


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
        client.stream.device.log.post()


Operation: POST /dataservice/stream/device/log/{logType}/{deviceUUID}/{sessionId}
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        payload: str, log_type: str, device_uuid: str, session_id: str
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
        client.stream.device.log.post()


.. toctree::
    :maxdepth: 1

    disable/index
    download
    renew/index
    search
    sessions/index
    type_
    models

