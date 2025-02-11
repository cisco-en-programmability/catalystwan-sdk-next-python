================================
multicloud.interconnect.gateways
================================


Operation: GET /dataservice/multicloud/interconnect/gateways
------------------------------------------------------------


API to retrieve all Interconnect Gateways from vManage.

.. code:: python

    def get_interconnect_gateways(
        interconnect_type: Optional[InterconnectTypeParam] = None,
        interconnect_account_id: Optional[str] = None,
        region: Optional[str] = None,
        region_id: Optional[str] = None,
        interconnect_gateway_name: Optional[str] = None,
        resource_state: Optional[str] = None,
        interconnect_billing_account_id: Optional[str] = None,
        refresh: Optional[str] = "false",
    ) -> List[InterconnectGatewayExtended]: ...


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
        client.multicloud.interconnect.gateways.get_interconnect_gateways()


Operation: POST /dataservice/multicloud/interconnect/gateways
-------------------------------------------------------------


API to create an Intercoonect gateway in an Interconnect provider.

.. code:: python

    def create_interconnect_gateway(
        payload: Optional[InterconnectGatewayExtended] = None,
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
        client.multicloud.interconnect.gateways.create_interconnect_gateway()


Operation: GET /dataservice/multicloud/interconnect/gateways/{interconnect-gateway-name}
----------------------------------------------------------------------------------------


API to retrieve the Interconnect Gateway Information from vManage.

.. code:: python

    def get_interconnect_gateway(
        interconnect_gateway_name: str,
    ) -> InterconnectGatewayExtended: ...


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
        client.multicloud.interconnect.gateways.get_interconnect_gateway()


Operation: PUT /dataservice/multicloud/interconnect/gateways/{interconnect-gateway-name}
----------------------------------------------------------------------------------------


API to update the Interconnect Gateway Information in vManage.

.. code:: python

    def update_interconnect_gateway(
        interconnect_gateway_name: str,
        payload: Optional[InterconnectGatewayExtended] = None,
    ) -> InterconnectGatewayExtended: ...


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
        client.multicloud.interconnect.gateways.update_interconnect_gateway()


Operation: DELETE /dataservice/multicloud/interconnect/gateways/{interconnect-gateway-name}
-------------------------------------------------------------------------------------------


API to delete an Interconnect Gateway from an Interconnect provider.

.. code:: python

    def delete_interconnect_gateway(
        interconnect_gateway_name: str,
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
        client.multicloud.interconnect.gateways.delete_interconnect_gateway()


.. toctree::
    :maxdepth: 1

    config_group/index
    image_names/index
    instance_sizes/index
    push_config/index
    types/index
    settings/index
    device_chassis_numbers/index
    devices/index
    models

