==============================
certificate.controller.bulkcsr
==============================


Operation: POST /dataservice/certificate/controller/bulkcsr
-----------------------------------------------------------


Generate CSR for all controller

.. code:: python

    def post(csr_key_length: Optional[str] = None) -> str: ...


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
        client.certificate.controller.bulkcsr.post()


