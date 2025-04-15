===================================
sslproxy.settings.enterprise.rootca
===================================


Operation: GET /dataservice/sslproxy/settings/enterprise/rootca
---------------------------------------------------------------


Get vManage enterprise root certificate

.. code:: python

    def get() -> Any: ...


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
        client.sslproxy.settings.enterprise.rootca.get()


Operation: POST /dataservice/sslproxy/settings/enterprise/rootca
----------------------------------------------------------------


Set vManage enterprise root certificate

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
        client.sslproxy.settings.enterprise.rootca.post()


