===============================
settings.client_session_timeout
===============================


Operation: GET /dataservice/settings/clientSessionTimeout
---------------------------------------------------------


Get client session timeout

.. code:: python

    def get() -> str: ...


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
        client.settings.client_session_timeout.get()


