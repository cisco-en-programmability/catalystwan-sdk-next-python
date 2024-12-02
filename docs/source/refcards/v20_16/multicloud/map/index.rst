==============
multicloud.map
==============


Operation: GET /dataservice/multicloud/map
------------------------------------------


Get Mapping details for cloudType

.. code:: python

    def get_mapping_matrix(
        cloud_type: CloudTypeParam,
    ) -> List[GetMapResponse]: ...


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
        client.multicloud.map.get_mapping_matrix()


Operation: POST /dataservice/multicloud/map
-------------------------------------------


Enable Mapping for cloudType

.. code:: python

    def process_mapping(
        payload: Optional[PostMapRequest] = None,
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
        client.multicloud.map.process_mapping()


.. toctree::
    :maxdepth: 1

    defaults/index
    status/index
    summary/index
    tags/index
    vpns/index
    models

