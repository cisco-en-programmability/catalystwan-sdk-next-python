====================================================
v1.feature_profile.sdwan.transport.ipv6_trackergroup
====================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup
----------------------------------------------------------------------------------------------


Get IPv6 TrackerGroup Profile Parcels for Transport feature profile

.. code:: python

    def get_ipv6_tracker_group_profile_parcel_for_transport(
        transport_id: str,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.get_ipv6_tracker_group_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup
-----------------------------------------------------------------------------------------------


Create a IPv6 TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def create_ipv6_tracker_group_profile_parcel_for_transport(
        transport_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.create_ipv6_tracker_group_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------


Get IPv6 TrackerGroup Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_ipv6_tracker_group_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, ipv6_trackergroup_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.get_ipv6_tracker_group_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------


Update a IPv6 TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def edit_ipv6_tracker_group_profile_parcel_for_transport(
        transport_id: str,
        ipv6_trackergroup_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.edit_ipv6_tracker_group_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-trackergroup/{ipv6-trackergroupId}
-----------------------------------------------------------------------------------------------------------------------


Delete a IPv6 TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def delete_ipv6_tracker_group_profile_parcel_for_transport(
        transport_id: str, ipv6_trackergroup_id: str
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
        client.v1.feature_profile.sdwan.transport.ipv6_trackergroup.delete_ipv6_tracker_group_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

