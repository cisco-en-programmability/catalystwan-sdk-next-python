========================
certificate.generate.csr
========================


Operation: POST /dataservice/certificate/generate/csr
-----------------------------------------------------


get certificaate details

.. code:: python

    def generate_csr(payload: Optional[Any] = None) -> str: ...


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
        client.certificate.generate.csr.generate_csr()


