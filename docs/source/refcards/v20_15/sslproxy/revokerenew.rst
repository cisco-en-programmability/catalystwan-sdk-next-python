====================
sslproxy.revokerenew
====================


Operation: POST /dataservice/sslproxy/revokerenew
-------------------------------------------------


Revoke and renew device certificate

.. code:: python

    def revoke_renew_certificate(
        payload: Optional[Any] = None,
    ) -> Any: ...


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
        client.sslproxy.revokerenew.revoke_renew_certificate()


