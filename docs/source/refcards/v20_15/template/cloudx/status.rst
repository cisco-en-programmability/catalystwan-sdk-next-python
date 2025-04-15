======================
template.cloudx.status
======================


Operation: GET /dataservice/template/cloudx/status
--------------------------------------------------


Get sites per application per vpn

.. code:: python

    def get(app_name: str, vpn_id: Optional[int] = None) -> List[Any]: ...


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
        client.template.cloudx.status.get()


