===============================
certificate.install.signed_cert
===============================


Operation: POST /dataservice/certificate/install/signedCert
-----------------------------------------------------------


install Certificate

.. code:: python

    def install_certificate(payload: Optional[Any] = None) -> str: ...


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
        client.certificate.install.signed_cert.install_certificate()


