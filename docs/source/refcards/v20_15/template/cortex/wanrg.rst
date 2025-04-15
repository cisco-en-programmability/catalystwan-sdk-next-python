=====================
template.cortex.wanrg
=====================


Operation: GET /dataservice/template/cortex/wanrg
-------------------------------------------------


Get WAN Resource Groups

.. code:: python

    def get(accountid: str) -> Any: ...


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
        client.template.cortex.wanrg.get()


Operation: PUT /dataservice/template/cortex/wanrg
-------------------------------------------------


Edit WAN Resource Groups

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.template.cortex.wanrg.put()


Operation: POST /dataservice/template/cortex/wanrg
--------------------------------------------------


Create WAN Resource Groups

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
        client.template.cortex.wanrg.post()


Operation: DELETE /dataservice/template/cortex/wanrg
----------------------------------------------------


Delete WAN Resource Groups

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
        client.template.cortex.wanrg.delete()


