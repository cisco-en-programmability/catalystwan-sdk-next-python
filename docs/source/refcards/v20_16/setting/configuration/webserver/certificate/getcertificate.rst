==========================================================
setting.configuration.webserver.certificate.getcertificate
==========================================================


Operation: GET /dataservice/setting/configuration/webserver/certificate/getcertificate
--------------------------------------------------------------------------------------


Get certificate for alias server

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
        client.setting.configuration.webserver.certificate.getcertificate.get()


