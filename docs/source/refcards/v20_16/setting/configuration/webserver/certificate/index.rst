===========================================
setting.configuration.webserver.certificate
===========================================


Operation: GET /dataservice/setting/configuration/webserver/certificate
-----------------------------------------------------------------------


Retrieves Certificate Signing Request information

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
        client.setting.configuration.webserver.certificate.get()


Operation: PUT /dataservice/setting/configuration/webserver/certificate
-----------------------------------------------------------------------


Import a signed web server certificate

.. code:: python

    def put(payload: Any) -> str: ...


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
        client.setting.configuration.webserver.certificate.put()


Operation: POST /dataservice/setting/configuration/webserver/certificate
------------------------------------------------------------------------


Generate Certificate Signing Request

.. code:: python

    def post(payload: Any) -> str: ...


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
        client.setting.configuration.webserver.certificate.post()


.. toctree::
    :maxdepth: 1

    getcertificate

