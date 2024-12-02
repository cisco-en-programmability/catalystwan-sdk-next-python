=======================
multicloud.hostvpc.tags
=======================


Operation: GET /dataservice/multicloud/hostvpc/tags
---------------------------------------------------


Get VPC Tags

.. code:: python

    def get_vpc_tags(
        cloud_type: Optional[str] = None,
        region: Optional[str] = None,
        tag_name: Optional[str] = None,
    ) -> List[HostVpcTagResponse]: ...


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
        client.multicloud.hostvpc.tags.get_vpc_tags()


Operation: PUT /dataservice/multicloud/hostvpc/tags
---------------------------------------------------


Edit VPCs for a Tag

.. code:: python

    def edit_tag(payload: Optional[HostVpcTagPut] = None) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.edit_tag()


Operation: POST /dataservice/multicloud/hostvpc/tags
----------------------------------------------------


Tag a VPC

.. code:: python

    def host_vpc_tagging(
        payload: Optional[HostVpcTagPost] = None,
    ) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.host_vpc_tagging()


Operation: DELETE /dataservice/multicloud/hostvpc/tags/{tagName}
----------------------------------------------------------------


Delete a Tag

.. code:: python

    def un_tag(tag_name: str) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.un_tag()


.. toctree::
    :maxdepth: 1

    rebalance_vnets/index
    models

