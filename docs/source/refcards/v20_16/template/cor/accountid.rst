======================
template.cor.accountid
======================


Operation: DELETE /dataservice/template/cor/accountid/{accountid}
-----------------------------------------------------------------


Deprecated!!!

Delete transit VPC/VNet

.. code:: python

    def remove_transit_vpc(
        accountid: str,
        transitvpcid: str,
        cloudregion: str,
        cloudtype: Optional[str] = "AWS",
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
        client.template.cor.accountid.remove_transit_vpc()


