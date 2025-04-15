================================
multicloud.cloudgateway.resource
================================


Operation: GET /dataservice/multicloud/cloudgateway/resource
------------------------------------------------------------


Discover Resource of CGW

.. code:: python

    def get(cloud_gateway_name: str) -> List[CgwResourceResponse]: ...


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
        client.multicloud.cloudgateway.resource.get()


.. toctree::
    :maxdepth: 1

    models

