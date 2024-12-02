=============================
multicloud.cloudgateway.vwans
=============================


Operation: GET /dataservice/multicloud/cloudgateway/vwans
---------------------------------------------------------


Discover Azure Virtual WANS

.. code:: python

    def get_azure_virtual_wans(
        cloud_type: str,
        account_id: str,
        resource_group_name: str,
        resource_group_source: str,
    ) -> List[VwanListResponse]: ...


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
        client.multicloud.cloudgateway.vwans.get_azure_virtual_wans()


.. toctree::
    :maxdepth: 1

    models

