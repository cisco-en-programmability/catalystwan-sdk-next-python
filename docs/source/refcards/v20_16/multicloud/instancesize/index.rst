=======================
multicloud.instancesize
=======================


Operation: GET /dataservice/multicloud/instancesize
---------------------------------------------------


Get Transit VPC supported size

.. code:: python

    def get_supported_instance_size(
        cloud_type: CloudTypeParam,
        account_id: Optional[str] = None,
        cloud_region: Optional[str] = None,
    ) -> List[InstanceSizeResponse]: ...


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
        client.multicloud.instancesize.get_supported_instance_size()


.. toctree::
    :maxdepth: 1

    edge/index
    models

