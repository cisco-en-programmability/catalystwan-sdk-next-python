==================
multicloud.hostvpc
==================


Operation: GET /dataservice/multicloud/hostvpc
----------------------------------------------


Get all Host VPCs

.. code:: python

    def get_host_vpcs(
        cloud_type: str,
        account_ids: Optional[str] = None,
        region: Optional[str] = None,
        untagged: Optional[str] = None,
    ) -> List[HostVpcsResponse]: ...


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
        client.multicloud.hostvpc.get_host_vpcs()


.. toctree::
    :maxdepth: 1

    tags/index
    models

