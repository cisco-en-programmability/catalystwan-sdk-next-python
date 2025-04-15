==============================
multicloud.cloudgateway.nvasku
==============================


Operation: GET /dataservice/multicloud/cloudgateway/nvasku
----------------------------------------------------------


Get Azure NVA SKUs

.. code:: python

    def get(cloud_type: str) -> NvaSkuListResponse: ...


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
        client.multicloud.cloudgateway.nvasku.get()


.. toctree::
    :maxdepth: 1

    models

