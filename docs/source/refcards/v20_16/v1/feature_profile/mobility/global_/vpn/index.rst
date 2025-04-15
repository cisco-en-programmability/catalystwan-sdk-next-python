=======================================
v1.feature_profile.mobility.global_.vpn
=======================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn
-------------------------------------------------------------------------------


Create a VPN Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateVpnProfileParcelForMobilityPostRequest,
    ) -> CreateVpnProfileParcelForMobilityPostResponse: ...


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
        client.v1.feature_profile.mobility.global_.vpn.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}
--------------------------------------------------------------------------------------


Update a VPN Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        vpn_id: str,
        payload: EditVpnProfileParcelForMobilityPutRequest,
    ) -> EditVpnProfileParcelForMobilityPutResponse: ...


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
        client.v1.feature_profile.mobility.global_.vpn.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}
-----------------------------------------------------------------------------------------


Delete a VPN Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, vpn_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.vpn.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn
------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(profile_id: str) -> GetListMobilityGlobalVpnPayload: ...


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
        client.v1.feature_profile.mobility.global_.vpn.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}
--------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, vpn_id: str
    ) -> GetSingleMobilityGlobalVpnPayload: ...


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
        client.v1.feature_profile.mobility.global_.vpn.get()


.. toctree::
    :maxdepth: 1

    models

