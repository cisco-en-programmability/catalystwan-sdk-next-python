===============================================
multicloud.interconnect.gateways.instance_sizes
===============================================


Operation: GET /dataservice/multicloud/interconnect/gateways/instance-sizes
---------------------------------------------------------------------------


API to retrieve Interconnect Gateway instance sizes supported by an  Interconnect provider.

.. code:: python

    def get(
        interconnect_type: InterconnectTypeParam,
    ) -> InlineResponse2004: ...


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
        client.multicloud.interconnect.gateways.instance_sizes.get()


.. toctree::
    :maxdepth: 1

    models

