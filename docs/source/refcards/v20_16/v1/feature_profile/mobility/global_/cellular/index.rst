============================================
v1.feature_profile.mobility.global_.cellular
============================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular
-----------------------------------------------------------------------------------


Get an Mobility Cellular Profile Parcel list for Mobility Global Feature Profile

.. code:: python

    def get_cellular_profile_parcel_list_for_mobility(
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
        client.v1.feature_profile.mobility.global_.cellular.get_cellular_profile_parcel_list_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular
------------------------------------------------------------------------------------


Create an cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_cellular_profile_parcel_for_mobility(
        profile_id: str, payload: Optional[CellularProfile] = None
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
        client.v1.feature_profile.mobility.global_.cellular.create_cellular_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}
------------------------------------------------------------------------------------------------


Get an Mobility Cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def get_cellular_profile_parcel_for_mobility(
        profile_id: str, cellular_id: str
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
        client.v1.feature_profile.mobility.global_.cellular.get_cellular_profile_parcel_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}
------------------------------------------------------------------------------------------------


Edit an Cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def edit_cellular_profile_parcel_for_mobility(
        profile_id: str,
        cellular_id: str,
        payload: Optional[
            EditCellularProfileParcelForMobilityPutRequest
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
        client.v1.feature_profile.mobility.global_.cellular.edit_cellular_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}
---------------------------------------------------------------------------------------------------


Delete a Cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete_a_cellular_profile_parcel_for_mobility(
        profile_id: str, cellular_id: str
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
        client.v1.feature_profile.mobility.global_.cellular.delete_a_cellular_profile_parcel_for_mobility()


.. toctree::
    :maxdepth: 1

    models

