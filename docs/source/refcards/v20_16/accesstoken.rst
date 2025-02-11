===========
accesstoken
===========


Operation: GET /dataservice/accesstoken/{regionBaseUri}/{clientId}
------------------------------------------------------------------


Get Access Token for SecureX Ribbon

.. code:: python

    def get_secure_x_access_token(
        client_id: str, region_base_uri: str
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
        client.accesstoken.get_secure_x_access_token()


