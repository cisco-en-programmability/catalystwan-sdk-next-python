=======================================
multicloud.cloudgateway.resource_groups
=======================================


Operation: GET /dataservice/multicloud/cloudgateway/resourceGroups
------------------------------------------------------------------


Discover Azure Resource Groups

.. code:: python

    def get(
        cloud_type: str, account_id: str
    ) -> List[ResourceGroupsResponse]: ...


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
        client.multicloud.cloudgateway.resource_groups.get()


.. toctree::
    :maxdepth: 1

    models

