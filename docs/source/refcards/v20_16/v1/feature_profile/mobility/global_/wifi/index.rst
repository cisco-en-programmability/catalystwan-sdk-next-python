========================================
v1.feature_profile.mobility.global_.wifi
========================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi
-------------------------------------------------------------------------------


Get Wifi Profile Parcel List for Mobility feature profile

.. code:: python

    def get_wifi_profile_parcel_list_for_mobility(
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
        client.v1.feature_profile.mobility.global_.wifi.get_wifi_profile_parcel_list_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi
--------------------------------------------------------------------------------


Create an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def create_wifi_profile_parcel_for_mobility(
        profile_id: str,
        payload: Optional[
            CreateWifiProfileParcelForMobilityPostRequest
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
        client.v1.feature_profile.mobility.global_.wifi.create_wifi_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}
----------------------------------------------------------------------------------------


Get an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def get_wifi_profile_parcel_for_mobility(
        profile_id: str, wifi_id: str
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
        client.v1.feature_profile.mobility.global_.wifi.get_wifi_profile_parcel_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}
----------------------------------------------------------------------------------------


Edit an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def edit_wifi_profile_parcel_for_mobility(
        profile_id: str,
        wifi_id: str,
        payload: Optional[
            CreateWifiProfileParcelForMobilityPostRequest
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
        client.v1.feature_profile.mobility.global_.wifi.edit_wifi_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}
-------------------------------------------------------------------------------------------


Delete an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def delete_wifi_profile_parcel_for_mobility(
        profile_id: str, wifi_id: str
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
        client.v1.feature_profile.mobility.global_.wifi.delete_wifi_profile_parcel_for_mobility()


.. toctree::
    :maxdepth: 1

    models

