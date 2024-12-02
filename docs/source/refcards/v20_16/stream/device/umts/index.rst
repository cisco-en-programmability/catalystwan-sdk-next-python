==================
stream.device.umts
==================


Operation: POST /dataservice/stream/device/umts
-----------------------------------------------


assign sessionId to client if there is no conflict ongoing sessions

.. code:: python

    def enable_session(
        payload: Optional[UmtsInput] = None,
    ) -> List[UmtsSession]: ...


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
        client.stream.device.umts.enable_session()


Operation: GET /dataservice/stream/device/umts/{operation}/{sessionId}
----------------------------------------------------------------------


start, stop,status,download or disable session

.. code:: python

    def update_umts_session_status(
        operation: str, session_id: str
    ) -> Any: ...


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
        client.stream.device.umts.update_umts_session_status()


.. toctree::
    :maxdepth: 1

    statistics
    save
    models

