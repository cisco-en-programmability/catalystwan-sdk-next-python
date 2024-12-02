==============================
multicloud.cloudgateway.nvasku
==============================


Operation: GET /dataservice/multicloud/cloudgateway/nvasku
----------------------------------------------------------


Get Azure NVA SKUs

.. code:: python

    def get_azure_nva_sku_resources(
        cloud_type: str,
    ) -> NvaSkuListResponse: ...


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
        client.multicloud.cloudgateway.nvasku.get_azure_nva_sku_resources()


.. toctree::
    :maxdepth: 1

    models

