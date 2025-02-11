==========================================================
v1.feature_profile.sdwan.transport.esimcellular_controller
==========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller
----------------------------------------------------------------------------------------------------


Get eSim Cellular Controller Features for Transport feature profile

.. code:: python

    def get_esim_cellular_controller_profile_feature_for_transport(
        transport_id: str,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.get_esim_cellular_controller_profile_feature_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller
-----------------------------------------------------------------------------------------------------


Create a eSim Cellular Controller Feature for Transport feature profile

.. code:: python

    def create_esim_cellular_controller_profile_feature_for_transport(
        transport_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.create_esim_cellular_controller_profile_feature_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}
-------------------------------------------------------------------------------------------------------------------------------


Get eSim Cellular Controller Feature by Feature Id for Transport feature profile

.. code:: python

    def get_esim_cellular_controller_profile_feature_by_feature_id_for_transport(
        transport_id: str, esim_cellular_controller_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.get_esim_cellular_controller_profile_feature_by_feature_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}
-------------------------------------------------------------------------------------------------------------------------------


Update a eSim Cellular Controller Feature for Transport feature profile

.. code:: python

    def edit_esim_cellular_controller_profile_feature_for_transport(
        transport_id: str,
        esim_cellular_controller_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.edit_esim_cellular_controller_profile_feature_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}
----------------------------------------------------------------------------------------------------------------------------------


Delete a eSim Cellular Controller Feature for Transport feature profile

.. code:: python

    def delete_esim_cellular_controller_profile_feature_for_transport(
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
        client.v1.feature_profile.sdwan.transport.esimcellular_controller.delete_esim_cellular_controller_profile_feature_for_transport()


