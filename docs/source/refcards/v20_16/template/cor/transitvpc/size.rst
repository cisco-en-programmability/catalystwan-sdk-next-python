============================
template.cor.transitvpc.size
============================


Operation: GET /dataservice/template/cor/transitvpc/size
--------------------------------------------------------


Deprecated!!!

Get transit VPC supported size

.. code:: python

    def get_transit_vpc_supported_size(
        cloud_environment: str, cloudtype: Optional[str] = "AWS"
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
        client.template.cor.transitvpc.size.get_transit_vpc_supported_size()


