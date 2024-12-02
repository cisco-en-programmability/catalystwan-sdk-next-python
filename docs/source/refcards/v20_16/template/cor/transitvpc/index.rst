=======================
template.cor.transitvpc
=======================


Operation: GET /dataservice/template/cor/transitvpc
---------------------------------------------------


Deprecated!!!

Get transit VPC/VNet list

.. code:: python

    def get_transit_vp_cs(
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
        client.template.cor.transitvpc.get_transit_vp_cs()


Operation: PUT /dataservice/template/cor/transitvpc
---------------------------------------------------


Deprecated!!!

Update transit VPC/VNet

.. code:: python

    def update_transit_vpc(payload: Optional[Any] = None) -> Any: ...


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
        client.template.cor.transitvpc.update_transit_vpc()


Operation: POST /dataservice/template/cor/transitvpc
----------------------------------------------------


Deprecated!!!

Create transit VPC/VNet

.. code:: python

    def add_transit_vpc(payload: Optional[Any] = None) -> Any: ...


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
        client.template.cor.transitvpc.add_transit_vpc()


.. toctree::
    :maxdepth: 1

    autoscale_properties
    size

