====================
template.cortex.sync
====================


Operation: POST /dataservice/template/cortex/sync
-------------------------------------------------


Sync WAN Resource Groups

.. code:: python

    def sync_wan_resource_groups(
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
        client.template.cortex.sync.sync_wan_resource_groups()


