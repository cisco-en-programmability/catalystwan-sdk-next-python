=======================================================
v1.feature_profile.sdwan.transport.esimcellular_profile
=======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile
-------------------------------------------------------------------------------------------------


Get EsimCellular Profile Features for Transport feature profile

.. code:: python

    def get_esim_cellular_profile_profile_feature_for_transport(
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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.get_esim_cellular_profile_profile_feature_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile
--------------------------------------------------------------------------------------------------


Create a EsimCellular Profile Feature for Transport feature profile

.. code:: python

    def create_esim_cellular_profile_profile_feature_for_transport(
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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.create_esim_cellular_profile_profile_feature_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}
-------------------------------------------------------------------------------------------------------------------------


Get EsimCellular Profile Feature by Feature Id for Transport feature profile

.. code:: python

    def get_esim_cellular_profile_by_feature_id_for_transport(
        transport_id: str, esim_cellular_profile_id: str
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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.get_esim_cellular_profile_by_feature_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}
-------------------------------------------------------------------------------------------------------------------------


Update a EsimCellular Profile Feature for Transport feature profile

.. code:: python

    def edit_esim_cellular_profile_profile_feature_for_transport(
        transport_id: str,
        esim_cellular_profile_id: str,
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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.edit_esim_cellular_profile_profile_feature_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}
----------------------------------------------------------------------------------------------------------------------------


Delete a EsimCellular Profile Feature for Transport feature profile

.. code:: python

    def delete_esim_cellular_profile_profile_feature_for_transport(
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
        client.v1.feature_profile.sdwan.transport.esimcellular_profile.delete_esim_cellular_profile_profile_feature_for_transport()


