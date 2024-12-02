========================================
multicloud.cloud_routers_and_attachments
========================================


Operation: GET /dataservice/multicloud/cloudRoutersAndAttachments
-----------------------------------------------------------------


Deprecated!!!

Get all Cloud Routers and their Attachments

.. code:: python

    def get_cloud_routers_and_attachments(
        account_id: Optional[str] = None,
        region: Optional[str] = None,
        network: Optional[str] = None,
        connectivity_gateway_name: Optional[str] = None,
        cloud_gateway_name: Optional[str] = None,
        state: Optional[str] = None,
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
        client.multicloud.cloud_routers_and_attachments.get_cloud_routers_and_attachments()


