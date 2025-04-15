=============================================================
v1.feature_profile.sd_routing.transport.multicloud_connection
=============================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection
--------------------------------------------------------------------------------------------------------


Associate a MultiCloudConnection Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str, payload: CreateMultiCloudConnection1PostRequest
    ) -> CreateMultiCloudConnection1PostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}
--------------------------------------------------------------------------------------------------------------------------------


Update a multicloud connection parcel

.. code:: python

    def put(
        transport_id: str,
        multi_cloud_connection_id: str,
        payload: EditMultiCloudConnection1PutRequest,
    ) -> EditMultiCloudConnection1PutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}
-----------------------------------------------------------------------------------------------------------------------------------


Delete a MultiCloud Connection Profile Parcel for Transport feature profile

.. code:: python

    def delete(
        transport_id: str, multi_cloud_connection_id: str
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection
-------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportVrfWanMulticloudConnectionPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}
--------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, multi_cloud_connection_id: str
    ) -> GetSingleSdRoutingTransportVrfWanMulticloudConnectionPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.get()


.. toctree::
    :maxdepth: 1

    models

