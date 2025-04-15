===============
multicloud.vwan
===============


Operation: POST /dataservice/multicloud/vwan
--------------------------------------------


Deprecated!!!

Create Virtual WAN

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
        client.multicloud.vwan.post()


Operation: DELETE /dataservice/multicloud/vwan/{cloudProvider}/{vWanName}
-------------------------------------------------------------------------


Deprecated!!!

Delete Virtual Wan

.. code:: python

    def delete(
        cloud_provider: str,
        v_wan_name: str,
        account_id: Optional[str] = None,
        resource_group: Optional[str] = None,
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
        client.multicloud.vwan.delete()


