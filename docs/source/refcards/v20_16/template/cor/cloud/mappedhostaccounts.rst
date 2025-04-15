=====================================
template.cor.cloud.mappedhostaccounts
=====================================


Operation: GET /dataservice/template/cor/cloud/mappedhostaccounts
-----------------------------------------------------------------


Deprecated!!!

Get cloud mapped accounts view

.. code:: python

    def get(accountid: str, cloudtype: str) -> Any: ...


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
        client.template.cor.cloud.mappedhostaccounts.get()


