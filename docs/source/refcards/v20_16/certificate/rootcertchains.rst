==========================
certificate.rootcertchains
==========================


Operation: GET /dataservice/certificate/rootcertchains
------------------------------------------------------


get root cert chain in the system

.. code:: python

    def get(action: str) -> List[str]: ...


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
        client.certificate.rootcertchains.get()


Operation: PUT /dataservice/certificate/rootcertchains
------------------------------------------------------


save root cert chain in the system

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
        client.certificate.rootcertchains.put()


