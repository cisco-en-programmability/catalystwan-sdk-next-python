============
client.token
============


Operation: GET /dataservice/client/token
----------------------------------------


Get CSRF token

.. code:: python

    def get(json: Optional[bool] = False) -> ClientTokenResponse: ...


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
        client.client.token.get()


.. toctree::
    :maxdepth: 1

    models

