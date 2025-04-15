=================
certificate.vedge
=================


Operation: GET /dataservice/certificate/vedge
---------------------------------------------


get device installed cert

.. code:: python

    def get(uuid: str) -> List[InstalledCertsInner]: ...


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
        client.certificate.vedge.get()


.. toctree::
    :maxdepth: 1

    csr
    list
    models

