==============================================
v1.feature_profile.mobility.global_.aaaservers
==============================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers
--------------------------------------------------------------------------------------


Create a aaaservers Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateAaaServersProfileParcelForMobilityPostRequest,
    ) -> CreateAaaServersProfileParcelForMobilityPostResponse: ...


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
        client.v1.feature_profile.mobility.global_.aaaservers.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers/{aaaserversId}
----------------------------------------------------------------------------------------------------


Update a aaaservers Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        aaaservers_id: str,
        payload: EditAaaServersProfileParcelForMobilityPutRequest,
    ) -> EditAaaServersProfileParcelForMobilityPutResponse: ...


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
        client.v1.feature_profile.mobility.global_.aaaservers.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers/{aaaserversId}
-------------------------------------------------------------------------------------------------------


Delete a aaaservers Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, aaaservers_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.aaaservers.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str,
    ) -> GetListMobilityGlobalAaaserversPayload: ...


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
        client.v1.feature_profile.mobility.global_.aaaservers.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/aaaservers/{aaaserversId}
----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, aaaservers_id: str
    ) -> GetSingleMobilityGlobalAaaserversPayload: ...


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
        client.v1.feature_profile.mobility.global_.aaaservers.get()


.. toctree::
    :maxdepth: 1

    models

