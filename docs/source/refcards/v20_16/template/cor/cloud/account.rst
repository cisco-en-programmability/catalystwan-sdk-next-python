==========================
template.cor.cloud.account
==========================


Operation: GET /dataservice/template/cor/cloud/account
------------------------------------------------------


Deprecated!!!

Get cloud accounts

.. code:: python

    def get(cloudtype: str, cloud_environment: str) -> Any: ...


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
        client.template.cor.cloud.account.get()


