=======================
template.cor.transitvpc
=======================


Operation: GET /dataservice/template/cor/transitvpc
---------------------------------------------------


Deprecated!!!

Get transit VPC/VNet list

.. code:: python

    def get(
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
        client.template.cor.transitvpc.get()


Operation: PUT /dataservice/template/cor/transitvpc
---------------------------------------------------


Deprecated!!!

Update transit VPC/VNet

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.template.cor.transitvpc.put()


Operation: POST /dataservice/template/cor/transitvpc
----------------------------------------------------


Deprecated!!!

Create transit VPC/VNet

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.cor.transitvpc.post()


.. toctree::
    :maxdepth: 1

    autoscale_properties
    size

