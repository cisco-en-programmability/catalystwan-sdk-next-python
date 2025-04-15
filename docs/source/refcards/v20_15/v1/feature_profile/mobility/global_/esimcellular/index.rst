================================================
v1.feature_profile.mobility.global_.esimcellular
================================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular
----------------------------------------------------------------------------------------


Create a EsimCellular Profile Feature for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateEsimCellularProfileFeatureForMobilityPostRequest,
    ) -> CreateEsimCellularProfileFeatureForMobilityPostResponse: ...


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
        client.v1.feature_profile.mobility.global_.esimcellular.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}
--------------------------------------------------------------------------------------------------------


Update a EsimCellular Profile Feature for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        esim_cellular_id: str,
        payload: EditEsimCellularProfileFeatureForMobilityPutRequest,
    ) -> EditEsimCellularProfileFeatureForMobilityPutResponse: ...


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
        client.v1.feature_profile.mobility.global_.esimcellular.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}
-----------------------------------------------------------------------------------------------------------


Delete a EsimCellular Profile Feature for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, esim_cellular_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.esimcellular.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular
---------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str,
    ) -> GetListMobilityGlobalEsimcellularPayload: ...


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
        client.v1.feature_profile.mobility.global_.esimcellular.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, esim_cellular_id: str
    ) -> GetSingleMobilityGlobalEsimcellularPayload: ...


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
        client.v1.feature_profile.mobility.global_.esimcellular.get()


.. toctree::
    :maxdepth: 1

    models

