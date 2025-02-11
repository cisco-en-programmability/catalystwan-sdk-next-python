===========================================
setting.configuration.webserver.certificate
===========================================


Operation: GET /dataservice/setting/configuration/webserver/certificate
-----------------------------------------------------------------------


Retrieves Certificate Signing Request information

.. code:: python

    def show_info() -> str: ...


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
        client.setting.configuration.webserver.certificate.show_info()


Operation: PUT /dataservice/setting/configuration/webserver/certificate
-----------------------------------------------------------------------


Import a signed web server certificate

.. code:: python

    def import_certificate(payload: Optional[Any] = None) -> str: ...


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
        client.setting.configuration.webserver.certificate.import_certificate()


Operation: POST /dataservice/setting/configuration/webserver/certificate
------------------------------------------------------------------------


Generate Certificate Signing Request

.. code:: python

    def get_csr(payload: Optional[Any] = None) -> str: ...


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
        client.setting.configuration.webserver.certificate.get_csr()


.. toctree::
    :maxdepth: 1

    getcertificate

