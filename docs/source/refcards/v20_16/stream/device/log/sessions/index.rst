==========================
stream.device.log.sessions
==========================


Operation: GET /dataservice/stream/device/log/sessions
------------------------------------------------------


.. code:: python

    def get() -> None: ...


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
        client.stream.device.log.sessions.get()


.. toctree::
    :maxdepth: 1

    clear

