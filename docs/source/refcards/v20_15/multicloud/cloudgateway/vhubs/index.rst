=============================
multicloud.cloudgateway.vhubs
=============================


Operation: GET /dataservice/multicloud/cloudgateway/vhubs
---------------------------------------------------------


Discover Azure Virtual HUBs

.. code:: python

    def get(
        cloud_type: str,
        account_id: str,
        region: str,
        resource_group_name: str,
        resource_group_source: str,
        vwan_name: str,
        vwan_source: str,
    ) -> List[VhubsListResponse]: ...


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
        client.multicloud.cloudgateway.vhubs.get()


.. toctree::
    :maxdepth: 1

    models

