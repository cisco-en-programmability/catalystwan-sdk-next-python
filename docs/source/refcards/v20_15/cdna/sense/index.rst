==========
cdna.sense
==========


Operation: GET /dataservice/cdna/sense/{tag}
--------------------------------------------


Get Sense Service

.. code:: python

    def get_cdna_sense_service(tag: str) -> DnaSenseResponse: ...


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
        client.cdna.sense.get_cdna_sense_service()


.. toctree::
    :maxdepth: 1

    models

