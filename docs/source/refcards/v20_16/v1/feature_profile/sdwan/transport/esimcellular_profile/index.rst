=======================================================
v1.feature_profile.sdwan.transport.esimcellular_profile
=======================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile
--------------------------------------------------------------------------------------------------


Create a EsimCellular Profile Feature for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateEsimCellularProfileProfileFeatureForTransportPostRequest,
    ) -> (
        CreateEsimCellularProfileProfileFeatureForTransportPostResponse
    ): ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}
-------------------------------------------------------------------------------------------------------------------------


Update a EsimCellular Profile Feature for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        esim_cellular_profile_id: str,
        payload: EditEsimCellularProfileProfileFeatureForTransportPutRequest,
    ) -> EditEsimCellularProfileProfileFeatureForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}
----------------------------------------------------------------------------------------------------------------------------


Delete a EsimCellular Profile Feature for Transport feature profile

.. code:: python

    def delete(
        transport_id: str, esim_cellular_profile_id: str
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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile
-------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportEsimcellularProfilePayload: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}
-------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, esim_cellular_profile_id: str
    ) -> GetSingleSdwanTransportEsimcellularProfilePayload: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.get()


.. toctree::
    :maxdepth: 1

    models

