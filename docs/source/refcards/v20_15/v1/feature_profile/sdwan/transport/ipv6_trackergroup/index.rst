====================================================
v1.feature_profile.sdwan.transport.ipv6_trackergroup
====================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup
-----------------------------------------------------------------------------------------------


Create a IPv6 TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateIpv6TrackerGroupProfileParcelForTransportPostRequest,
    ) -> CreateIpv6TrackerGroupProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------


Update a IPv6 TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        ipv6_trackergroup_id: str,
        payload: EditIpv6TrackerGroupProfileParcelForTransportPutRequest,
    ) -> EditIpv6TrackerGroupProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup/{ipv6-trackergroupId}
-----------------------------------------------------------------------------------------------------------------------


Delete a IPv6 TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, ipv6_trackergroup_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportIpv6TrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ipv6_trackergroup_id: str
    ) -> GetSingleSdwanTransportIpv6TrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

