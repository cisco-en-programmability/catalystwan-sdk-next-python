===============================
certificate.forcesync.root_cert
===============================


Operation: POST /dataservice/certificate/forcesync/rootCert
-----------------------------------------------------------


force Sync RootCert to all devices

.. code:: python

    def force_sync_root_cert() -> str: ...


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
        client.certificate.forcesync.root_cert.force_sync_root_cert()


