=======================================
v1.feature_profile.mobility.global_.qos
=======================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{globalId}/qos
------------------------------------------------------------------------------


Create a Qos Feature for Global feature profile

.. code:: python

    def post(
        global_id: str, payload: CreateQosFeatureForGlobalPostRequest
    ) -> CreateQosFeatureForGlobalPostResponse: ...


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
        client.v1.feature_profile.mobility.global_.qos.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}
-------------------------------------------------------------------------------------


Update a Qos Feature for Global feature profile

.. code:: python

    def put(
        global_id: str,
        qos_id: str,
        payload: EditQosFeatureForGlobalPutRequest,
    ) -> EditQosFeatureForGlobalPutResponse: ...


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
        client.v1.feature_profile.mobility.global_.qos.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}
----------------------------------------------------------------------------------------


Delete a Qos Feature for Global feature profile

.. code:: python

    def delete(global_id: str, qos_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.qos.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{globalId}/qos
-----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(global_id: str) -> GetListMobilityGlobalQosPayload: ...


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
        client.v1.feature_profile.mobility.global_.qos.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        global_id: str, qos_id: str
    ) -> GetSingleMobilityGlobalQosPayload: ...


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
        client.v1.feature_profile.mobility.global_.qos.get()


.. toctree::
    :maxdepth: 1

    models

