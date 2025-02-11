=================
stream.device.log
=================


Operation: POST /dataservice/stream/device/log
----------------------------------------------


.. code:: python

    def get_session_info_log(payload: Optional[str] = None) -> None: ...


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
        client.stream.device.log.get_session_info_log()


Operation: POST /dataservice/stream/device/log/{logType}/{deviceUUID}/{sessionId}
---------------------------------------------------------------------------------


.. code:: python

    def stream_log(
        log_type: str,
        device_uuid: str,
        session_id: str,
        payload: Optional[str] = None,
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
        client.stream.device.log.stream_log()


Operation: GET /dataservice/stream/device/log/{sessionId}
---------------------------------------------------------


.. code:: python

    def get_device_log(
        session_id: Uuid, log_id: Optional[int] = -1
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
        client.stream.device.log.get_device_log()


.. toctree::
    :maxdepth: 1

    disable/index
    download
    renew/index
    search
    sessions/index
    type_
    models

