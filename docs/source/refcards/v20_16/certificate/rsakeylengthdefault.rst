===============================
certificate.rsakeylengthdefault
===============================


Operation: GET /dataservice/certificate/rsakeylengthdefault
-----------------------------------------------------------


Check if all devices in network use 2048-b RSA Key length for their device certs.

.. code:: python

    def rsa_key_length2048_for_all_devices() -> str: ...


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
        client.certificate.rsakeylengthdefault.rsa_key_length2048_for_all_devices()


