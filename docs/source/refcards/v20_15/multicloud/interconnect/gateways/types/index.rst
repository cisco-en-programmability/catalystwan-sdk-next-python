======================================
multicloud.interconnect.gateways.types
======================================


Operation: GET /dataservice/multicloud/interconnect/gateways/types
------------------------------------------------------------------


API to retrieve the supported Interconnect Gateway solution types.

.. code:: python

    def get_interconnet_gateway_types(
        interconnect_type: InterconnectTypeParam,
    ) -> List[str]: ...


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
        client.multicloud.interconnect.gateways.types.get_interconnet_gateway_types()


.. toctree::
    :maxdepth: 1

    models

