=====================
sslproxy.certificates
=====================


Operation: POST /dataservice/sslproxy/certificates
--------------------------------------------------


Upload device certificates

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
        client.sslproxy.certificates.post()


