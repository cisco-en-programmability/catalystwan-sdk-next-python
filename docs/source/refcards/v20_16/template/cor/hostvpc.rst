====================
template.cor.hostvpc
====================


Operation: GET /dataservice/template/cor/hostvpc
------------------------------------------------


Deprecated!!!

Get host VPC/VNet list

.. code:: python

    def get_cloud_host_vp_cs(
        accountid: str, cloudregion: str, cloudtype: Optional[str] = "AWS"
    ) -> List[Any]: ...


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
        client.template.cor.hostvpc.get_cloud_host_vp_cs()


