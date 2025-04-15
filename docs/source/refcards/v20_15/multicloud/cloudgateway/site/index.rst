============================
multicloud.cloudgateway.site
============================


Operation: GET /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
---------------------------------------------------------------------------


Get sites attached to CGW

.. code:: python

    def get(
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
        client.multicloud.cloudgateway.site.get()


Operation: PUT /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
---------------------------------------------------------------------------


Update tunnel scaling and accelerated vpn parameter for a branch endpoint

.. code:: python

    def put(
        cloud_gateway_name: str, payload: TunnelScalingRequestPayload
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
        client.multicloud.cloudgateway.site.put()


Operation: POST /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
----------------------------------------------------------------------------


Attach sites to Cloud Gateway

.. code:: python

    def post(
        cloud_gateway_name: str,
        payload: List[AttachSitesRequestPayloadInner],
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
        client.multicloud.cloudgateway.site.post()


Operation: DELETE /dataservice/multicloud/cloudgateway/{cloudGatewayName}/site
------------------------------------------------------------------------------


Detach sites from cloud gateway

.. code:: python

    def delete(
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
        client.multicloud.cloudgateway.site.delete()


.. toctree::
    :maxdepth: 1

    models

