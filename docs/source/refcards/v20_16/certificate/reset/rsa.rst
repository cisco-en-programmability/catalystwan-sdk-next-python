=====================
certificate.reset.rsa
=====================


Operation: POST /dataservice/certificate/reset/rsa
--------------------------------------------------


resetRSA for controllers

.. code:: python

    def reset_rsa(payload: Optional[str] = None) -> str: ...


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
        client.certificate.reset.rsa.reset_rsa()


