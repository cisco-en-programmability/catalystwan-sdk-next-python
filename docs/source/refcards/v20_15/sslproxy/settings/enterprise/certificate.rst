========================================
sslproxy.settings.enterprise.certificate
========================================


Operation: GET /dataservice/sslproxy/settings/enterprise/certificate
--------------------------------------------------------------------


Get enterprise certificate

.. code:: python

    def get_enterprise_certificate() -> Any: ...


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
        client.sslproxy.settings.enterprise.certificate.get_enterprise_certificate()


Operation: POST /dataservice/sslproxy/settings/enterprise/certificate
---------------------------------------------------------------------


Configure enterprise certificate

.. code:: python

    def set_enterprise_cert(payload: Optional[Any] = None) -> Any: ...


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
        client.sslproxy.settings.enterprise.certificate.set_enterprise_cert()


