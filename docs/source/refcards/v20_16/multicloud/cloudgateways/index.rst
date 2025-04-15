========================
multicloud.cloudgateways
========================


Operation: GET /dataservice/multicloud/cloudgateways/{cloudType}
----------------------------------------------------------------


Get sites with connectivity to the cloud by cloud type

.. code:: python

    def get(
        cloud_type: CloudTypeParam,
    ) -> List[CloudGatewayListResponse]: ...


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
        client.multicloud.cloudgateways.get()


.. toctree::
    :maxdepth: 1

    models

