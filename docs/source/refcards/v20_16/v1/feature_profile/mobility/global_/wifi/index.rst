========================================
v1.feature_profile.mobility.global_.wifi
========================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi
--------------------------------------------------------------------------------


Create an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateWifiProfileParcelForMobilityPostRequest,
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
        client.v1.feature_profile.mobility.global_.wifi.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}
----------------------------------------------------------------------------------------


Edit an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def put(
        profile_id: str,
        wifi_id: str,
        payload: EditWifiProfileParcelForMobilityPutRequest,
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
        client.v1.feature_profile.mobility.global_.wifi.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}
-------------------------------------------------------------------------------------------


Delete an Wifi Profile Parcel for Mobility feature profile

.. code:: python

    def delete(profile_id: str, wifi_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.wifi.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi
-------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(profile_id: str) -> GetListMobilityGlobalWifiPayload: ...


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
        client.v1.feature_profile.mobility.global_.wifi.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, wifi_id: str
    ) -> GetSingleMobilityGlobalWifiPayload: ...


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
        client.v1.feature_profile.mobility.global_.wifi.get()


.. toctree::
    :maxdepth: 1

    models

