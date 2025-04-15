===================================
v1.multicloud.interconnect.gateways
===================================


Operation: PUT /dataservice/v1/multicloud/interconnect/gateways/{interconnect-gateway-name}
-------------------------------------------------------------------------------------------


Asynchronous API to update the Interconnect Gateway Information in vManage.

.. code:: python

    def put(
        interconnect_gateway_name: str,
        payload: InterconnectGatewayExtended,
    ) -> ProcessResponse: ...


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
        client.v1.multicloud.interconnect.gateways.put()


.. toctree::
    :maxdepth: 1

    models

