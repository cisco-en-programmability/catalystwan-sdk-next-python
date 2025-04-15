=======================================
multicloud.hostvpc.tags.rebalance_vnets
=======================================


Operation: POST /dataservice/multicloud/hostvpc/tags/rebalanceVnets
-------------------------------------------------------------------


Tag a VPC

.. code:: python

    def post(cloud_type: str, region: str, tag_name: str) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.rebalance_vnets.post()


.. toctree::
    :maxdepth: 1

    models

