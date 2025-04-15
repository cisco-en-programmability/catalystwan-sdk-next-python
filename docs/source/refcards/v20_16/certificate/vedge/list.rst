======================
certificate.vedge.list
======================


Operation: GET /dataservice/certificate/vedge/list
--------------------------------------------------


get vEdge list

.. code:: python

    def get(state: Optional[str] = None) -> str: ...


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
        client.certificate.vedge.list.get()


Operation: POST /dataservice/certificate/vedge/list
---------------------------------------------------


Save vEdge list (send to controller)

.. code:: python

    def post(payload: str, action: Optional[str] = None) -> str: ...


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
        client.certificate.vedge.list.post()


