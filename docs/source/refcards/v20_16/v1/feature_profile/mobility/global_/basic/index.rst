=========================================
v1.feature_profile.mobility.global_.basic
=========================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/basic
--------------------------------------------------------------------------------


Get Basic Profile Parcels for Mobility Global Feature Profile

.. code:: python

    def get_basic_profile_parcel_for_mobility(profile_id: str) -> str: ...


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
        client.v1.feature_profile.mobility.global_.basic.get_basic_profile_parcel_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/basic
---------------------------------------------------------------------------------


Create a Basic Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_basic_profile_parcel_for_mobility(
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
        client.v1.feature_profile.mobility.global_.basic.create_basic_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}
-------------------------------------------------------------------------------------------


Get Basic Profile Parcel by parcelId for Mobility Global Feature Profile

.. code:: python

    def get_basic_profile_parcel_by_parcel_id_for_mobility(
        profile_id: str, parcel_id: str
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
        client.v1.feature_profile.mobility.global_.basic.get_basic_profile_parcel_by_parcel_id_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}
-------------------------------------------------------------------------------------------


Update a Basic Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def edit_basic_profile_parcel_for_mobility(
        profile_id: str, parcel_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.basic.edit_basic_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}
----------------------------------------------------------------------------------------------


Delete a Basic Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete_basic_profile_parcel_for_mobility(
        profile_id: str, parcel_id: str
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
        client.v1.feature_profile.mobility.global_.basic.delete_basic_profile_parcel_for_mobility()


.. toctree::
    :maxdepth: 1

    schema/index

