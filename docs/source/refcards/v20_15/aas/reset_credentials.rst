=====================
aas.reset_credentials
=====================


Operation: POST /dataservice/aas/reset-credentials/{credType}
-------------------------------------------------------------


SDWAN as a Platform - Manage Credentials

.. code:: python

    def post(cred_type: str) -> None: ...


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
        client.aas.reset_credentials.post()


