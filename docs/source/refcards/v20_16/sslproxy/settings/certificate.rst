=============================
sslproxy.settings.certificate
=============================


Operation: GET /dataservice/sslproxy/settings/certificate
---------------------------------------------------------


Get certificate state

.. code:: python

    def get() -> Any: ...


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
        client.sslproxy.settings.certificate.get()


