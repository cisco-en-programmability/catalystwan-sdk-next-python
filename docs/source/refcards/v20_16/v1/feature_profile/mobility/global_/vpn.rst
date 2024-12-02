=======================================
v1.feature_profile.mobility.global_.vpn
=======================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn
------------------------------------------------------------------------------


Get VPN Profile Parcels for Mobility Global Feature Profile

.. code:: python

    def get_vpn_profile_parcel_for_mobility(profile_id: str) -> str: ...


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
        client.v1.feature_profile.mobility.global_.vpn.get_vpn_profile_parcel_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn
-------------------------------------------------------------------------------


Create a VPN Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_vpn_profile_parcel_for_mobility(
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
        client.v1.feature_profile.mobility.global_.vpn.create_vpn_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}
--------------------------------------------------------------------------------------


Get VPN Profile Parcel by parcelId for Mobility Global Feature Profile

.. code:: python

    def get_vpn_profile_parcel_by_parcel_id_for_mobility(
        profile_id: str, vpn_id: str
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
        client.v1.feature_profile.mobility.global_.vpn.get_vpn_profile_parcel_by_parcel_id_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}
--------------------------------------------------------------------------------------


Update a VPN Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def edit_vpn_profile_parcel_for_mobility(
        profile_id: str, vpn_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.vpn.edit_vpn_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}
-----------------------------------------------------------------------------------------


Delete a VPN Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete_vpn_profile_parcel_for_mobility(
        profile_id: str, vpn_id: str
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
        client.v1.feature_profile.mobility.global_.vpn.delete_vpn_profile_parcel_for_mobility()


