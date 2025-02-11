=============================
sslproxy.settings.vmanage.csr
=============================


Operation: GET /dataservice/sslproxy/settings/vmanage/csr
---------------------------------------------------------


Get vManage CSR

.. code:: python

    def getv_manage_csr() -> Any: ...


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
        client.sslproxy.settings.vmanage.csr.getv_manage_csr()


