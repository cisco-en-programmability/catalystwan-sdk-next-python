==========================
certificate.rootcertchains
==========================


Operation: GET /dataservice/certificate/rootcertchains
------------------------------------------------------


get root cert chain in the system

.. code:: python

    def get_root_cert_chains(action: str) -> List[str]: ...


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
        client.certificate.rootcertchains.get_root_cert_chains()


Operation: PUT /dataservice/certificate/rootcertchains
------------------------------------------------------


save root cert chain in the system

.. code:: python

    def save_root_cert_chain(payload: Optional[str] = None) -> str: ...


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
        client.certificate.rootcertchains.save_root_cert_chain()


