============================================
multicloud.interconnect.cloud.accounts.vhubs
============================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vhubs
--------------------------------------------------------------------------------------------------------


API to retrieve Azure Virtual Hubs.

.. code:: python

    def get(
        cloud_type: str,
        cloud_account_id: str,
        resource_group: Optional[str] = None,
        refresh: Optional[str] = "false",
        vwan_name: Optional[str] = None,
        tag_name: Optional[str] = None,
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
        client.multicloud.interconnect.cloud.accounts.vhubs.get()


