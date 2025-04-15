===========================================
multicloud.cloudgateway.vnets_noof_attached
===========================================


Operation: GET /dataservice/multicloud/cloudgateway/vnetsNoofAttached
---------------------------------------------------------------------


Discover Azure Virtual HUBs

.. code:: python

    def get(
        cloud_type: str, cloud_gateway_name: str
    ) -> IsVnetAttached: ...


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
        client.multicloud.cloudgateway.vnets_noof_attached.get()


.. toctree::
    :maxdepth: 1

    models

