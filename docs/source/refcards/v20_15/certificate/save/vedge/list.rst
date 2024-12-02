===========================
certificate.save.vedge.list
===========================


Operation: POST /dataservice/certificate/save/vedge/list
--------------------------------------------------------


change VedgeList Validity

.. code:: python

    def save_v_edge_list(payload: Optional[str] = None) -> str: ...


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
        client.certificate.save.vedge.list.save_v_edge_list()


