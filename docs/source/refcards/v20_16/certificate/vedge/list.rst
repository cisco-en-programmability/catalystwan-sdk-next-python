======================
certificate.vedge.list
======================


Operation: GET /dataservice/certificate/vedge/list
--------------------------------------------------


get vEdge list

.. code:: python

    def getv_edge_list(state: Optional[str] = None) -> str: ...


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
        client.certificate.vedge.list.getv_edge_list()


Operation: POST /dataservice/certificate/vedge/list
---------------------------------------------------


Save vEdge list (send to controller)

.. code:: python

    def setv_edge_list(
        payload: Optional[str] = None, action: Optional[str] = None
    ) -> str: ...


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
        client.certificate.vedge.list.setv_edge_list()


