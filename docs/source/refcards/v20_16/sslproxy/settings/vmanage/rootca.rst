================================
sslproxy.settings.vmanage.rootca
================================


Operation: GET /dataservice/sslproxy/settings/vmanage/rootca
------------------------------------------------------------


Get vManage root certificate

.. code:: python

    def getv_manage_root_ca() -> Any: ...


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
        client.sslproxy.settings.vmanage.rootca.getv_manage_root_ca()


Operation: POST /dataservice/sslproxy/settings/vmanage/rootca
-------------------------------------------------------------


Set vManage root certificate

.. code:: python

    def setv_manage_root_ca(payload: Optional[Any] = None) -> Any: ...


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
        client.sslproxy.settings.vmanage.rootca.setv_manage_root_ca()


