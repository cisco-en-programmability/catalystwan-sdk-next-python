===========================================
v1.feature_profile.sdwan.service.switchport
===========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport
------------------------------------------------------------------------------------


Create a switchport Parcel to a service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CedgeServiceProfileSwitchportParcelRestfulResourcePostRequest,
    ) -> (
        CedgeServiceProfileSwitchportParcelRestfulResourcePostResponse
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
        client.v1.feature_profile.sdwan.service.switchport.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}
--------------------------------------------------------------------------------------------------


Update a Switchport Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        switchport_id: str,
        payload: EditSwitchportParcelAssociationForServicePutRequest,
    ) -> EditSwitchportParcelAssociationForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.switchport.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}
-----------------------------------------------------------------------------------------------------


Delete a Switchport Parcel for service feature profile

.. code:: python

    def delete(service_id: str, switchport_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.switchport.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport
-----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceSwitchportPayload: ...


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
        client.v1.feature_profile.sdwan.service.switchport.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}
--------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, switchport_id: str
    ) -> GetSingleSdwanServiceSwitchportPayload: ...


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
        client.v1.feature_profile.sdwan.service.switchport.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

