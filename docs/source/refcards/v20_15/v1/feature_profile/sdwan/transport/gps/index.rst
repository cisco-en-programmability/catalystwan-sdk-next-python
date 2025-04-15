======================================
v1.feature_profile.sdwan.transport.gps
======================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps
---------------------------------------------------------------------------------


Create a Gps Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateGpsProfileParcelForTransportPostRequest,
    ) -> CreateGpsProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.gps.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}
----------------------------------------------------------------------------------------


Update a Gps Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        gps_id: str,
        payload: EditGpsProfileParcelForTransportPutRequest,
    ) -> EditGpsProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.gps.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}
-------------------------------------------------------------------------------------------


Delete a Gps Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, gps_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.gps.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps
--------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetListSdwanTransportGpsPayload: ...


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
        client.v1.feature_profile.sdwan.transport.gps.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, gps_id: str
    ) -> GetSingleSdwanTransportGpsPayload: ...


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
        client.v1.feature_profile.sdwan.transport.gps.get()


.. toctree::
    :maxdepth: 1

    models

