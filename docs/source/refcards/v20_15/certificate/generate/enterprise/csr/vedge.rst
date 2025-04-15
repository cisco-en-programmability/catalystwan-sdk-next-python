=========================================
certificate.generate.enterprise.csr.vedge
=========================================


Operation: POST /dataservice/certificate/generate/enterprise/csr/vedge
----------------------------------------------------------------------


generate CSR on hardware WAN edge device

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
        client.certificate.generate.enterprise.csr.vedge.post()


