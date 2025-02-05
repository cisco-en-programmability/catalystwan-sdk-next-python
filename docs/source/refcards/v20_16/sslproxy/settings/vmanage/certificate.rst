=====================================
sslproxy.settings.vmanage.certificate
=====================================


Operation: GET /dataservice/sslproxy/settings/vmanage/certificate
-----------------------------------------------------------------


Get vManage intermediate certificate

.. code:: python

    def getv_manage_certificate() -> Any: ...


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
        client.sslproxy.settings.vmanage.certificate.getv_manage_certificate()


Operation: POST /dataservice/sslproxy/settings/vmanage/certificate
------------------------------------------------------------------


Set vManage root certificate

.. code:: python

    def setv_manageintermediate_cert(
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
        client.sslproxy.settings.vmanage.certificate.setv_manageintermediate_cert()


