===================================
sslproxy.settings.enterprise.rootca
===================================


Operation: GET /dataservice/sslproxy/settings/enterprise/rootca
---------------------------------------------------------------


Get vManage enterprise root certificate

.. code:: python

    def get_v_manage_enterprise_root_certificate() -> Any: ...


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
        client.sslproxy.settings.enterprise.rootca.get_v_manage_enterprise_root_certificate()


Operation: POST /dataservice/sslproxy/settings/enterprise/rootca
----------------------------------------------------------------


Set vManage enterprise root certificate

.. code:: python

    def set_enterprise_root_ca_cert(
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
        client.sslproxy.settings.enterprise.rootca.set_enterprise_root_ca_cert()


