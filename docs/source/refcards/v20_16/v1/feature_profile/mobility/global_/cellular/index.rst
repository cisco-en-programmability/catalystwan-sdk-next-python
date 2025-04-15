============================================
v1.feature_profile.mobility.global_.cellular
============================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular
------------------------------------------------------------------------------------


Create an cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(profile_id: str, payload: CellularProfile) -> str: ...


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
        client.v1.feature_profile.mobility.global_.cellular.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}
------------------------------------------------------------------------------------------------


Edit an Cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        cellular_id: str,
        payload: EditCellularProfileParcelForMobilityPutRequest,
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
        client.v1.feature_profile.mobility.global_.cellular.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}
---------------------------------------------------------------------------------------------------


Delete a Cellular Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, cellular_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.cellular.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular
-----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(profile_id: str) -> GetListMobilityGlobalCellularPayload: ...


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
        client.v1.feature_profile.mobility.global_.cellular.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, cellular_id: str
    ) -> GetSingleMobilityGlobalCellularPayload: ...


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
        client.v1.feature_profile.mobility.global_.cellular.get()


.. toctree::
    :maxdepth: 1

    models

