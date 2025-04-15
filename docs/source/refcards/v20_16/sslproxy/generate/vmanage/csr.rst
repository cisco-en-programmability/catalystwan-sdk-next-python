=============================
sslproxy.generate.vmanage.csr
=============================


Operation: POST /dataservice/sslproxy/generate/vmanage/csr
----------------------------------------------------------


Generate CSR

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.sslproxy.generate.vmanage.csr.post()


