===================================================
v1.feature_profile.sdwan.transport.t1_e1_controller
===================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller
----------------------------------------------------------------------------------------------


Create a T1e1controller Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateT1E1ControllerProfileParcelForTransportPostRequest,
    ) -> CreateT1E1ControllerProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}
----------------------------------------------------------------------------------------------------------------


Update a T1e1controller Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        t1e1controller_id: str,
        payload: EditT1E1ControllerProfileParcelForTransportPutRequest,
    ) -> EditT1E1ControllerProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}
-------------------------------------------------------------------------------------------------------------------


Delete a T1e1controller Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, t1e1controller_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportT1E1ControllerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, t1e1controller_id: str
    ) -> GetSingleSdwanTransportT1E1ControllerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

