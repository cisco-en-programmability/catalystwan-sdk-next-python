===================================================
v1.feature_profile.sdwan.transport.cellular_profile
===================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile
----------------------------------------------------------------------------------------------


Create a Cellular Profile Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateCellularProfileProfileParcelForTransportPostRequest,
    ) -> CreateCellularProfileProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_profile.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId}
-----------------------------------------------------------------------------------------------------------------


Update a Cellular Profile Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        cellular_profile_id: str,
        payload: EditCellularProfileProfileParcelForTransportPutRequest,
    ) -> EditCellularProfileProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_profile.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId}
--------------------------------------------------------------------------------------------------------------------


Delete a Cellular Profile Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, cellular_profile_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_profile.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportCellularProfilePayload: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_profile.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_profile_id: str
    ) -> GetSingleSdwanTransportCellularProfilePayload: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_profile.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

