=======================
multicloud.cloudgateway
=======================


Operation: GET /dataservice/multicloud/cloudgateway
---------------------------------------------------


Get cloud gateways

.. code:: python

    def get_cgws(
        cloud_type: Optional[str] = None,
        account_id: Optional[str] = None,
        region: Optional[str] = None,
        cloud_gateway_name: Optional[str] = None,
        connectivity_state: Optional[str] = None,
    ) -> List[CloudGatewayListResponse]: ...


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
        client.multicloud.cloudgateway.get_cgws()


Operation: POST /dataservice/multicloud/cloudgateway
----------------------------------------------------


Create cloud gateway

.. code:: python

    def create_cgw(
        payload: Optional[CloudGatewayPost] = None,
    ) -> Taskid: ...


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
        client.multicloud.cloudgateway.create_cgw()


Operation: GET /dataservice/multicloud/cloudgateway/{cloudGatewayName}
----------------------------------------------------------------------


Get cloud gateway by name

.. code:: python

    def get_cgw_details(
        cloud_gateway_name: str,
    ) -> CloudGatewayAdjusted: ...


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
        client.multicloud.cloudgateway.get_cgw_details()


Operation: PUT /dataservice/multicloud/cloudgateway/{cloudGatewayName}
----------------------------------------------------------------------


Update cloud gateway

.. code:: python

    def update_cgw(
        cloud_gateway_name: str, payload: Optional[UpdateCgw] = None
    ) -> Taskid: ...


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
        client.multicloud.cloudgateway.update_cgw()


Operation: DELETE /dataservice/multicloud/cloudgateway/{cloudGatewayName}
-------------------------------------------------------------------------


Delete cloud gateway

.. code:: python

    def delete_cgw(
        cloud_gateway_name: str,
        delete_all_resources: Optional[str] = "true",
    ) -> Taskid: ...


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
        client.multicloud.cloudgateway.delete_cgw()


.. toctree::
    :maxdepth: 1

    config_group/index
    nva_security_rules/index
    nvas/index
    nvasku/index
    resource/index
    resource_groups/index
    vhubs/index
    vnets_noof_attached/index
    vpn_gateways/index
    vwans/index
    site/index
    gateways/index
    models

