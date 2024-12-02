=====================
certificate.vedge.csr
=====================


Operation: GET /dataservice/certificate/vedge/csr
-------------------------------------------------


get device CSR

.. code:: python

    def getv_edge_csr(uuid: str) -> str: ...


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
        client.certificate.vedge.csr.getv_edge_csr()


