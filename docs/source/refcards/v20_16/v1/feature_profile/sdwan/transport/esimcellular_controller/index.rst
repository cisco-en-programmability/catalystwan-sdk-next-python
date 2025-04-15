==========================================================
v1.feature_profile.sdwan.transport.esimcellular_controller
==========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller
-----------------------------------------------------------------------------------------------------


Create a eSim Cellular Controller Feature for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateEsimCellularControllerProfileFeatureForTransportPostRequest,
    ) -> (
        CreateEsimCellularControllerProfileFeatureForTransportPostResponse
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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}
-------------------------------------------------------------------------------------------------------------------------------


Update a eSim Cellular Controller Feature for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        esim_cellular_controller_id: str,
        payload: EditEsimCellularControllerProfileFeatureForTransportPutRequest,
    ) -> (
        EditEsimCellularControllerProfileFeatureForTransportPutResponse
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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}
----------------------------------------------------------------------------------------------------------------------------------


Delete a eSim Cellular Controller Feature for Transport feature profile

.. code:: python

    def delete(
        transport_id: str, esim_cellular_controller_id: str
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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller
----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportEsimcellularControllerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}
-------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, esim_cellular_controller_id: str
    ) -> GetSingleSdwanTransportEsimcellularControllerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.get()


.. toctree::
    :maxdepth: 1

    models

