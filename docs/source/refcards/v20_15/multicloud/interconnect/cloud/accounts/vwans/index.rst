============================================
multicloud.interconnect.cloud.accounts.vwans
============================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans
--------------------------------------------------------------------------------------------------------


API to retrieve Azure Virtual Wans.

.. code:: python

    def get_az_virtual_wans(
        cloud_type: str,
        cloud_account_id: str,
        resource_group: str,
        refresh: Optional[str] = "false",
        vwan_name: Optional[str] = None,
    ) -> InlineResponse2009: ...


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
        client.multicloud.interconnect.cloud.accounts.vwans.get_az_virtual_wans()


Operation: POST /dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans
---------------------------------------------------------------------------------------------------------


API to create an Azure Virtual Wan..

.. code:: python

    def create_az_virtual_wan(
        cloud_type: str,
        cloud_account_id: str,
        payload: Optional[AzureVirtualWan] = None,
    ) -> InlineResponse2009: ...


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
        client.multicloud.interconnect.cloud.accounts.vwans.create_az_virtual_wan()


Operation: DELETE /dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans/{vwan-name}
-----------------------------------------------------------------------------------------------------------------------


API to delete an Azure Virtual Wan.

.. code:: python

    def delete_az_virtual_wan(
        cloud_type: CloudTypeParam,
        cloud_account_id: str,
        vwan_name: str,
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
        client.multicloud.interconnect.cloud.accounts.vwans.delete_az_virtual_wan()


.. toctree::
    :maxdepth: 1

    models

