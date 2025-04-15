===========================================
v1.feature_profile.mobility.global_.logging
===========================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/logging
-----------------------------------------------------------------------------------


Create a Logging Profile Feature for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateLoggingProfileFeatureForMobilityPostRequest,
    ) -> CreateLoggingProfileFeatureForMobilityPostResponse: ...


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
        client.v1.feature_profile.mobility.global_.logging.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Update a Logging Profile Feature for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        logging_id: str,
        payload: EditLoggingProfileFeatureForMobilityPutRequest,
    ) -> EditLoggingProfileFeatureForMobilityPutResponse: ...


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
        client.v1.feature_profile.mobility.global_.logging.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}
-------------------------------------------------------------------------------------------------


Delete a Logging Profile Feature for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, logging_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.logging.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/logging
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(profile_id: str) -> GetListMobilityGlobalLoggingPayload: ...


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
        client.v1.feature_profile.mobility.global_.logging.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, logging_id: str
    ) -> GetSingleMobilityGlobalLoggingPayload: ...


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
        client.v1.feature_profile.mobility.global_.logging.get()


.. toctree::
    :maxdepth: 1

    models

