===============================================
v1.feature_profile.sdwan.transport.ipv6_tracker
===============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker
-----------------------------------------------------------------------------------------


Get IPv6 Tracker Profile Parcels for Transport feature profile

.. code:: python

    def get_ipv6_tracker_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.get_ipv6_tracker_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker
------------------------------------------------------------------------------------------


Create a IPv6 Tracker Profile Parcel for Transport feature profile

.. code:: python

    def create_ipv6_tracker_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.create_ipv6_tracker_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------


Get IPv6 Tracker Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_ipv6_tracker_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, ipv6_tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.get_ipv6_tracker_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------


Update a IPv6 Tracker Profile Parcel for Transport feature profile

.. code:: python

    def edit_ipv6_tracker_profile_parcel_for_transport(
        transport_id: str,
        ipv6_tracker_id: str,
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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.edit_ipv6_tracker_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/ipv6-tracker/{ipv6-trackerId}
-------------------------------------------------------------------------------------------------------------


Delete a IPv6 Tracker Profile Parcel for Transport feature profile

.. code:: python

    def delete_ipv6_tracker_profile_parcel_for_transport(
        transport_id: str, ipv6_tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.ipv6_tracker.delete_ipv6_tracker_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

