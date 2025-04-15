===============================================
v1.feature_profile.sdwan.transport.ipv6_tracker
===============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker
------------------------------------------------------------------------------------------


Create a IPv6 Tracker Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateIpv6TrackerProfileParcelForTransportPostRequest,
    ) -> CreateIpv6TrackerProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------


Update a IPv6 Tracker Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        ipv6_tracker_id: str,
        payload: EditIpv6TrackerProfileParcelForTransportPutRequest,
    ) -> EditIpv6TrackerProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker/{ipv6-trackerId}
-------------------------------------------------------------------------------------------------------------


Delete a IPv6 Tracker Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, ipv6_tracker_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportIpv6TrackerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ipv6_tracker_id: str
    ) -> GetSingleSdwanTransportIpv6TrackerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

