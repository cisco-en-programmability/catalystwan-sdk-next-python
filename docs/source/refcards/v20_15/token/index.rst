=====
token
=====


Operation: POST /dataservice/token/{regionBaseUri}/{clientId}
-------------------------------------------------------------


Get Access Token and Refresh Token for authorized user

.. code:: python

    def token(client_id: str, region_base_uri: str) -> Tokens: ...


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
        client.token.token()


.. toctree::
    :maxdepth: 1

    models

