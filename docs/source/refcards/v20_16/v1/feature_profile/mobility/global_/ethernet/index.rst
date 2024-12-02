============================================
v1.feature_profile.mobility.global_.ethernet
============================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet
-----------------------------------------------------------------------------------


Get Ethernet Profile Parcels for feature profile

.. code:: python

    def get_ethernet_profile_parcels(profile_id: str) -> str: ...


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
        client.v1.feature_profile.mobility.global_.ethernet.get_ethernet_profile_parcels()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet
------------------------------------------------------------------------------------


Create an ethernet Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_ethernet_profile_parcel_for_mobility(
        profile_id: str,
        payload: Optional[
            CreateEthernetProfileParcelForMobilityPostRequest
        ] = None,
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
        client.v1.feature_profile.mobility.global_.ethernet.create_ethernet_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------


Get Ethernet Profile Parcels for feature profile

.. code:: python

    def get_ethernet_profile_parcel(
        profile_id: str, ethernet_id: str
    ) -> CreateEthernetProfileParcelForMobilityPostRequest: ...


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
        client.v1.feature_profile.mobility.global_.ethernet.get_ethernet_profile_parcel()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------


Update a Ethernet Profile Parcel for feature profile

.. code:: python

    def edit_ethernet_profile_parcel_for_system(
        profile_id: str,
        ethernet_id: str,
        payload: Optional[
            CreateEthernetProfileParcelForMobilityPostRequest
        ] = None,
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
        client.v1.feature_profile.mobility.global_.ethernet.edit_ethernet_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}
---------------------------------------------------------------------------------------------------


Delete a Ethernet Profile Parcel for feature profile

.. code:: python

    def delete_ethernet_profile_parcel_for_system(
        profile_id: str, ethernet_id: str
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
        client.v1.feature_profile.mobility.global_.ethernet.delete_ethernet_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    models

