==============
sslproxy.renew
==============


Operation: POST /dataservice/sslproxy/renew
-------------------------------------------


Renew device certificate

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.sslproxy.renew.post()


