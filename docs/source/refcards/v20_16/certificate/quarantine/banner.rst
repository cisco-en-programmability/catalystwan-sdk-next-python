=============================
certificate.quarantine.banner
=============================


Operation: GET /dataservice/certificate/quarantine/banner
---------------------------------------------------------


get quarantine banner data

.. code:: python

    def get() -> List[str]: ...


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
        client.certificate.quarantine.banner.get()


