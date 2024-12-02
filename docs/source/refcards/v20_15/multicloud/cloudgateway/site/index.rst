============================
multicloud.cloudgateway.site
============================


Operation: GET /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
---------------------------------------------------------------------------


Get sites attached to CGW

.. code:: python

    def get_cgw_attached_sites(
        cloud_gateway_name: str,
        system_ip: Optional[str] = None,
        site_id: Optional[str] = None,
        color: Optional[str] = None,
        vpn_tunnel_status: Optional[str] = None,
        solution: Optional[str] = None,
    ) -> GetSitesResponse: ...


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
        client.multicloud.cloudgateway.site.get_cgw_attached_sites()


Operation: PUT /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
---------------------------------------------------------------------------


Update tunnel scaling and accelerated vpn parameter for a branch endpoint

.. code:: python

    def tunnel_scaling(
        cloud_gateway_name: str,
        payload: Optional[TunnelScalingRequestPayload] = None,
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
        client.multicloud.cloudgateway.site.tunnel_scaling()


Operation: POST /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
----------------------------------------------------------------------------


Attach sites to Cloud Gateway

.. code:: python

    def attach_sites(
        cloud_gateway_name: str,
        payload: Optional[List[AttachSitesRequestPayloadInner]] = None,
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
        client.multicloud.cloudgateway.site.attach_sites()


Operation: DELETE /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
------------------------------------------------------------------------------


Detach sites from cloud gateway

.. code:: python

    def detach_sites_1(
        cloud_gateway_name: str,
        payload: Optional[List[DetachSitesRequestPayloadInner]] = None,
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
        client.multicloud.cloudgateway.site.detach_sites_1()


.. toctree::
    :maxdepth: 1

    models

