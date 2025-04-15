=========================================
multicloud.interconnect.gateways.settings
=========================================


Operation: GET /dataservice/multicloud/interconnect/gateways/{interconnect-gateway-name}/settings
-------------------------------------------------------------------------------------------------


API to retrieve the custom settings specified for an Interconnect Gateway

.. code:: python

    def get(
        interconnect_gateway_name: str, interconnect_account_id: str
    ) -> InterconnectGatewaySettings: ...


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
        client.multicloud.interconnect.gateways.settings.get()


.. toctree::
    :maxdepth: 1

    models

