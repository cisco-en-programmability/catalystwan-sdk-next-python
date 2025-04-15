=========================================
v1.feature_profile.mobility.global_.basic
=========================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/basic
---------------------------------------------------------------------------------


Create a Basic Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateBasicProfileParcelForMobilityPostRequest,
    ) -> CreateBasicProfileParcelForMobilityPostResponse: ...


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
        client.v1.feature_profile.mobility.global_.basic.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}
-------------------------------------------------------------------------------------------


Update a Basic Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        parcel_id: str,
        payload: EditBasicProfileParcelForMobilityPutRequest,
    ) -> EditBasicProfileParcelForMobilityPutResponse: ...


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
        client.v1.feature_profile.mobility.global_.basic.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}
----------------------------------------------------------------------------------------------


Delete a Basic Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, parcel_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.basic.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/basic
--------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(profile_id: str) -> GetListMobilityGlobalBasicPayload: ...


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
        client.v1.feature_profile.mobility.global_.basic.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}
-------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, parcel_id: str
    ) -> GetSingleMobilityGlobalBasicPayload: ...


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
        client.v1.feature_profile.mobility.global_.basic.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

