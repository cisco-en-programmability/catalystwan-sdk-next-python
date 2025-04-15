=======================
certificate.csr.details
=======================


Operation: GET /dataservice/certificate/csr/details
---------------------------------------------------


Get CSR detail view

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
        client.certificate.csr.details.get()


