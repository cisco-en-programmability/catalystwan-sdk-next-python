==========
cdna.sense
==========


Operation: GET /dataservice/cdna/sense/{tag}
--------------------------------------------


Get Sense Service

.. code:: python

    def get(tag: str) -> DnaSenseResponse: ...


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
        client.cdna.sense.get()


.. toctree::
    :maxdepth: 1

    models

