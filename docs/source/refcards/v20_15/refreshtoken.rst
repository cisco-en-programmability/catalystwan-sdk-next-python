============
refreshtoken
============


Operation: GET /dataservice/refreshtoken/{regionBaseUri}/{clientId}
-------------------------------------------------------------------


Get Access Token for SecureX Ribbon

.. code:: python

    def get(client_id: str, region_base_uri: str) -> str: ...


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
        client.refreshtoken.get()


