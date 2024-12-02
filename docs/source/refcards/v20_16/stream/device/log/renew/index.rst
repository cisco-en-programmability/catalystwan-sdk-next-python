=======================
stream.device.log.renew
=======================


Operation: GET /dataservice/stream/device/log/renew/{sessionId}
---------------------------------------------------------------


.. code:: python

    def renew_session_info(session_id: Uuid) -> None: ...


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
        client.stream.device.log.renew.renew_session_info()


.. toctree::
    :maxdepth: 1

    models

