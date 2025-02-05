=============
sslproxy.list
=============


Operation: GET /dataservice/sslproxy/list
-----------------------------------------


Get SSL proxy certificate list

.. code:: python

    def get_ssl_proxy_list() -> List[Any]: ...


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
        client.sslproxy.list.get_ssl_proxy_list()


