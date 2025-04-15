=========================
stream.device.log.disable
=========================


Operation: GET /dataservice/stream/device/log/disable/{sessionId}
-----------------------------------------------------------------


.. code:: python

    def get(session_id: Uuid) -> None: ...


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
        client.stream.device.log.disable.get()


.. toctree::
    :maxdepth: 1

    models

