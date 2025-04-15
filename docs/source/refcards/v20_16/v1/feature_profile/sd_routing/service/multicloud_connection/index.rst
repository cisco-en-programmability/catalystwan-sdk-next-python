===========================================================
v1.feature_profile.sd_routing.service.multicloud_connection
===========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection
----------------------------------------------------------------------------------------------------


Associate a MultiCloudConnection Parcel for service feature profile

.. code:: python

    def post(
        service_id: str, payload: CreateMultiCloudConnectionPostRequest
    ) -> CreateMultiCloudConnectionPostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}
----------------------------------------------------------------------------------------------------------------------------


Update a multicloud connection parcel

.. code:: python

    def put(
        service_id: str,
        multi_cloud_connection_id: str,
        payload: EditMultiCloudConnectionPutRequest,
    ) -> EditMultiCloudConnectionPutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}
-------------------------------------------------------------------------------------------------------------------------------


Delete a MultiCloud Connection Profile Parcel for Service feature profile

.. code:: python

    def delete(
        service_id: str, multi_cloud_connection_id: str
    ) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection
---------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceVrfLanMulticloudConnectionPayload: ...


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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}
----------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, multi_cloud_connection_id: str
    ) -> GetSingleSdRoutingServiceVrfLanMulticloudConnectionPayload: ...


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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.get()


.. toctree::
    :maxdepth: 1

    models

