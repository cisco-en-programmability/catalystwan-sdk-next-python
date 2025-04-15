===============
certificate.jks
===============


Operation: PUT /dataservice/certificate/jks
-------------------------------------------


update JKS

.. code:: python

    def put(payload: str) -> str: ...


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
        client.certificate.jks.put()


