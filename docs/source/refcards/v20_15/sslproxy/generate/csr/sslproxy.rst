==============================
sslproxy.generate.csr.sslproxy
==============================


Operation: POST /dataservice/sslproxy/generate/csr/sslproxy
-----------------------------------------------------------


Deprecated!!!

CSR request SSL proxy for edge

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.sslproxy.generate.csr.sslproxy.post()


