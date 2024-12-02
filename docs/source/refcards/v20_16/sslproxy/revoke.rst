===============
sslproxy.revoke
===============


Operation: POST /dataservice/sslproxy/revoke
--------------------------------------------


Revoke device certificate

.. code:: python

    def revoke_certificate(payload: Optional[Any] = None) -> Any: ...


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
        client.sslproxy.revoke.revoke_certificate()


