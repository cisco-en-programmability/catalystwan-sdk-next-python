=========================
dca.cloudservices.idtoken
=========================


Operation: GET /dataservice/dca/cloudservices/idtoken
-----------------------------------------------------


Get DCA Id token

.. code:: python

    def get_id_token() -> Any: ...


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
        client.dca.cloudservices.idtoken.get_id_token()


Operation: POST /dataservice/dca/cloudservices/idtoken
------------------------------------------------------


Set DCA Id token

.. code:: python

    def store_id_token(payload: Optional[Any] = None) -> None: ...


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
        client.dca.cloudservices.idtoken.store_id_token()


