==================================
certificate.vmanage.selfsignedcert
==================================


Operation: GET /dataservice/certificate/vmanage/selfsignedcert
--------------------------------------------------------------


get vManage self signed cert

.. code:: python

    def get_self_signed_cert() -> str: ...


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
        client.certificate.vmanage.selfsignedcert.get_self_signed_cert()


