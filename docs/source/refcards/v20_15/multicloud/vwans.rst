================
multicloud.vwans
================


Operation: GET /dataservice/multicloud/vwans
--------------------------------------------


Deprecated!!!

Get Virtual Wans

.. code:: python

    def get(
        account_id: Optional[str] = None,
        cloud_type: Optional[str] = None,
        resource_group: Optional[str] = None,
        refresh: Optional[str] = None,
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
        client.multicloud.vwans.get()


