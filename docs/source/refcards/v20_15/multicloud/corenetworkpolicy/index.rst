============================
multicloud.corenetworkpolicy
============================


Operation: GET /dataservice/multicloud/corenetworkpolicy
--------------------------------------------------------


Get AWS Cloudwan core network policy

.. code:: python

    def get_cwan_core_network_policy() -> CoreNetworkPolicyResponse: ...


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
        client.multicloud.corenetworkpolicy.get_cwan_core_network_policy()


.. toctree::
    :maxdepth: 1

    models

