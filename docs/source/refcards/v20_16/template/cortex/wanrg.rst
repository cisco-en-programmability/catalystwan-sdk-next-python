=====================
template.cortex.wanrg
=====================


Operation: GET /dataservice/template/cortex/wanrg
-------------------------------------------------


Get WAN Resource Groups

.. code:: python

    def get_wan_resource_groups(accountid: str) -> Any: ...


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
        client.template.cortex.wanrg.get_wan_resource_groups()


Operation: PUT /dataservice/template/cortex/wanrg
-------------------------------------------------


Edit WAN Resource Groups

.. code:: python

    def edit_wan_resource_groups(
        payload: Optional[Any] = None,
    ) -> None: ...


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
        client.template.cortex.wanrg.edit_wan_resource_groups()


Operation: POST /dataservice/template/cortex/wanrg
--------------------------------------------------


Create WAN Resource Groups

.. code:: python

    def save_wan_resource_groups(
        payload: Optional[Any] = None,
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
        client.template.cortex.wanrg.save_wan_resource_groups()


Operation: DELETE /dataservice/template/cortex/wanrg
----------------------------------------------------


Delete WAN Resource Groups

.. code:: python

    def delete_wan_resource_groups(
        payload: Optional[Any] = None,
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
        client.template.cortex.wanrg.delete_wan_resource_groups()


