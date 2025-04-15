================
multicloud.vhubs
================


Operation: GET /dataservice/multicloud/vhubs
--------------------------------------------


Deprecated!!!

Get Virtual Hubs

.. code:: python

    def get(
        cloud_type: Optional[str] = None,
        account_id: Optional[str] = None,
        resource_group: Optional[str] = None,
        v_wan_name: Optional[str] = None,
        v_net_tags: Optional[str] = None,
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
        client.multicloud.vhubs.get()


