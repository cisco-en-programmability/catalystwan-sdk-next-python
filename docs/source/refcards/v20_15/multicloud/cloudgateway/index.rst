=======================
multicloud.cloudgateway
=======================


Operation: GET /dataservice/multicloud/cloudgateway
---------------------------------------------------


Get cloud gateways

.. code:: python

    def get_list(
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
        client.multicloud.cloudgateway.get_list()


Operation: POST /dataservice/multicloud/cloudgateway
----------------------------------------------------


Create cloud gateway

.. code:: python

    def post(payload: CloudGatewayPost) -> Taskid: ...


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
        client.multicloud.cloudgateway.post()


Operation: GET /dataservice/multicloud/cloudgateway/{cloudGatewayName}
----------------------------------------------------------------------


Get cloud gateway by name

.. code:: python

    def get(cloud_gateway_name: str) -> CloudGatewayAdjusted: ...


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
        client.multicloud.cloudgateway.get()


Operation: PUT /dataservice/multicloud/cloudgateway/{cloudGatewayName}
----------------------------------------------------------------------


Update cloud gateway

.. code:: python

    def put(cloud_gateway_name: str, payload: UpdateCgw) -> Taskid: ...


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
        client.multicloud.cloudgateway.put()


Operation: DELETE /dataservice/multicloud/cloudgateway/{cloudGatewayName}
-------------------------------------------------------------------------


Delete cloud gateway

.. code:: python

    def delete(
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
        client.multicloud.cloudgateway.delete()


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

