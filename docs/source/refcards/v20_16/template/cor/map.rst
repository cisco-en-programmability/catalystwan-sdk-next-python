================
template.cor.map
================


Operation: GET /dataservice/template/cor/map
--------------------------------------------


Deprecated!!!

Get mapped VPC/VNet list

.. code:: python

    def get(accountid: str, cloudregion: str) -> Any: ...


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
        client.template.cor.map.get()


Operation: POST /dataservice/template/cor/map
---------------------------------------------


Deprecated!!!

Map host to transit VPC/VNet

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
        client.template.cor.map.post()


Operation: DELETE /dataservice/template/cor/map
-----------------------------------------------


Deprecated!!!

Unmap host from transit VPC/VNet

.. code:: python

    def delete(payload: Optional[Any] = None) -> Any: ...


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
        client.template.cor.map.delete()


