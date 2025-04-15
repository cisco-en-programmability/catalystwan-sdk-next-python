================================
sslproxy.settings.vmanage.rootca
================================


Operation: GET /dataservice/sslproxy/settings/vmanage/rootca
------------------------------------------------------------


Get vManage root certificate

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
        client.sslproxy.settings.vmanage.rootca.get()


Operation: POST /dataservice/sslproxy/settings/vmanage/rootca
-------------------------------------------------------------


Set vManage root certificate

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
        client.sslproxy.settings.vmanage.rootca.post()


