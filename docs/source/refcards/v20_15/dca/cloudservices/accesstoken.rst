=============================
dca.cloudservices.accesstoken
=============================


Operation: GET /dataservice/dca/cloudservices/accesstoken
---------------------------------------------------------


Get DCA access token

.. code:: python

    def get_access_token() -> Any: ...


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
        client.dca.cloudservices.accesstoken.get_access_token()


Operation: POST /dataservice/dca/cloudservices/accesstoken
----------------------------------------------------------


Set DCA access token

.. code:: python

    def store_access_token(payload: Optional[Any] = None) -> None: ...


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
        client.dca.cloudservices.accesstoken.store_access_token()


