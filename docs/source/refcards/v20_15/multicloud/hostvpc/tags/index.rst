=======================
multicloud.hostvpc.tags
=======================


Operation: GET /dataservice/multicloud/hostvpc/tags
---------------------------------------------------


Get VPC Tags

.. code:: python

    def get(
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
        client.multicloud.hostvpc.tags.get()


Operation: PUT /dataservice/multicloud/hostvpc/tags
---------------------------------------------------


Edit VPCs for a Tag

.. code:: python

    def put(payload: HostVpcTagPut) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.put()


Operation: POST /dataservice/multicloud/hostvpc/tags
----------------------------------------------------


Tag a VPC

.. code:: python

    def post(payload: HostVpcTagPost) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.post()


Operation: DELETE /dataservice/multicloud/hostvpc/tags/{tagName}
----------------------------------------------------------------


Delete a Tag

.. code:: python

    def delete(tag_name: str) -> Taskid: ...


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
        client.multicloud.hostvpc.tags.delete()


.. toctree::
    :maxdepth: 1

    rebalance_vnets/index
    models

