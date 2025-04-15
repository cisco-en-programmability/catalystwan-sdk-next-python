=======================
certificate.certdetails
=======================


Operation: POST /dataservice/certificate/certdetails
----------------------------------------------------


get certificaate details

.. code:: python

    def post(payload: str) -> str: ...


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
        client.certificate.certdetails.post()


