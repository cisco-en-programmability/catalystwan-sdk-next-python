============================
multicloud.cloudgateway.nvas
============================


Operation: GET /dataservice/multicloud/cloudgateway/nvas
--------------------------------------------------------


Discover Azure Network Virtual Appliances

.. code:: python

    def get_azure_network_virtual_appliances(
        cloud_type: str,
        account_id: str,
        region: str,
        resource_group_name: str,
        resource_group_source: str,
        vhub_name: str,
        vhub_source: str,
    ) -> List[NvasResponse]: ...


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
        client.multicloud.cloudgateway.nvas.get_azure_network_virtual_appliances()


.. toctree::
    :maxdepth: 1

    models

