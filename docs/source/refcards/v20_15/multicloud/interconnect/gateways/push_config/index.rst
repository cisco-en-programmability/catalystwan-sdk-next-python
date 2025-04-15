============================================
multicloud.interconnect.gateways.push_config
============================================


Operation: POST /dataservice/multicloud/interconnect/gateways/push-config
-------------------------------------------------------------------------


API to initiate a configuration push for an Interconnect gateway.

.. code:: python

    def post(payload: GatewaysPushconfigBody) -> ProcessResponse: ...


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
        client.multicloud.interconnect.gateways.push_config.post()


.. toctree::
    :maxdepth: 1

    models

