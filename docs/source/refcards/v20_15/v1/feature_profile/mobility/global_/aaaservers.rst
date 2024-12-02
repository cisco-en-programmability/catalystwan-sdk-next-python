==============================================
v1.feature_profile.mobility.global_.aaaservers
==============================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers
-------------------------------------------------------------------------------------


Get aaaservers Profile Parcels for Mobility Global Feature Profile

.. code:: python

    def get_aaa_servers_profile_parcel_for_mobility(
        profile_id: str,
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
        client.v1.feature_profile.mobility.global_.aaaservers.get_aaa_servers_profile_parcel_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers
--------------------------------------------------------------------------------------


Create a aaaservers Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_aaa_servers_profile_parcel_for_mobility(
        profile_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.aaaservers.create_aaa_servers_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers/{aaaserversId}
----------------------------------------------------------------------------------------------------


Get aaaservers Profile Parcel by parcelId for Mobility Global Feature Profile

.. code:: python

    def get_aaa_servers_profile_parcel_by_parcel_id_for_mobility(
        profile_id: str, aaaservers_id: str
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
        client.v1.feature_profile.mobility.global_.aaaservers.get_aaa_servers_profile_parcel_by_parcel_id_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers/{aaaserversId}
----------------------------------------------------------------------------------------------------


Update a aaaservers Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def edit_aaa_servers_profile_parcel_for_mobility(
        profile_id: str, aaaservers_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.aaaservers.edit_aaa_servers_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers/{aaaserversId}
-------------------------------------------------------------------------------------------------------


Delete a aaaservers Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete_aaa_servers_profile_parcel_for_mobility(
        profile_id: str, aaaservers_id: str
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
        client.v1.feature_profile.mobility.global_.aaaservers.delete_aaa_servers_profile_parcel_for_mobility()


