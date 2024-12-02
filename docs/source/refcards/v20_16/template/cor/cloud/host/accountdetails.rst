======================================
template.cor.cloud.host.accountdetails
======================================


Operation: GET /dataservice/template/cor/cloud/host/accountdetails
------------------------------------------------------------------


Deprecated!!!

Get cloud host VPC account details

.. code:: python

    def get_cloud_host_vpc_account_details() -> Any: ...


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
        client.template.cor.cloud.host.accountdetails.get_cloud_host_vpc_account_details()


