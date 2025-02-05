===========================
ise.credentials.pxgrid.cert
===========================


Operation: GET /dataservice/ise/credentials/pxgrid/cert
-------------------------------------------------------


Retrieves Pxgrid Certificate

.. code:: python

    def get_pxgrid_cert() -> str: ...


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
        client.ise.credentials.pxgrid.cert.get_pxgrid_cert()


