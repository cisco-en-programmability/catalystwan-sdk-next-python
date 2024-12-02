=======================
certificate.certdetails
=======================


Operation: POST /dataservice/certificate/certdetails
----------------------------------------------------


get certificaate details

.. code:: python

    def get_cert_details(payload: Optional[str] = None) -> str: ...


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
        client.certificate.certdetails.get_cert_details()


