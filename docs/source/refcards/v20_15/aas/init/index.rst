========
aas.init
========


Operation: POST /dataservice/aas/init
-------------------------------------


Initialize SDWAN as a Platform

.. code:: python

    def init_aas_properties(
        payload: Optional[InitBlob] = None,
    ) -> None: ...


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
        client.aas.init.init_aas_properties()


.. toctree::
    :maxdepth: 1

    models

