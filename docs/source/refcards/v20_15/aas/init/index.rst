========
aas.init
========


Operation: POST /dataservice/aas/init
-------------------------------------


Initialize SDWAN as a Platform

.. code:: python

    def post(payload: InitBlob) -> None: ...


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
        client.aas.init.post()


.. toctree::
    :maxdepth: 1

    models

