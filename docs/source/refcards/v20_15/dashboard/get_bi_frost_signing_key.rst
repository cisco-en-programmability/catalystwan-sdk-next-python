==================================
dashboard.get_bi_frost_signing_key
==================================


Operation: GET /dataservice/dashboard/getBiFrostSigningKey
----------------------------------------------------------


Register Controller to BiFrost Dashboard (by Controller)

.. code:: python

    def get_bi_frost_signing_key(
        cd_client_token: Optional[str] = None,
    ) -> None: ...


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
        client.dashboard.get_bi_frost_signing_key.get_bi_frost_signing_key()


