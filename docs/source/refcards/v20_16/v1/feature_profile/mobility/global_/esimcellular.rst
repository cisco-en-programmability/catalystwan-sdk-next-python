================================================
v1.feature_profile.mobility.global_.esimcellular
================================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular
---------------------------------------------------------------------------------------


Get EsimCellular Profile Features for Mobility Global Feature Profile

.. code:: python

    def get_esim_cellular_profile_feature_for_mobility(
        profile_id: str,
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
        client.v1.feature_profile.mobility.global_.esimcellular.get_esim_cellular_profile_feature_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular
----------------------------------------------------------------------------------------


Create a EsimCellular Profile Feature for Mobility Global Feature Profile

.. code:: python

    def create_esim_cellular_profile_feature_for_mobility(
        profile_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.esimcellular.create_esim_cellular_profile_feature_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}
--------------------------------------------------------------------------------------------------------


Get EsimCellular Profile Feature by Feature Id for Mobility Global Feature Profile

.. code:: python

    def get_esim_cellular_profile_feature_by_esim_cellular_id_for_mobility(
        profile_id: str, esim_cellular_id: str
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
        client.v1.feature_profile.mobility.global_.esimcellular.get_esim_cellular_profile_feature_by_esim_cellular_id_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}
--------------------------------------------------------------------------------------------------------


Update a EsimCellular Profile Feature for Mobility Global Feature Profile

.. code:: python

    def edit_esim_cellular_profile_feature_for_mobility(
        profile_id: str,
        esim_cellular_id: str,
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
        client.v1.feature_profile.mobility.global_.esimcellular.edit_esim_cellular_profile_feature_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}
-----------------------------------------------------------------------------------------------------------


Delete a EsimCellular Profile Feature for Mobility Global Feature Profile

.. code:: python

    def delete_esim_cellular_profile_feature_for_mobility(
        profile_id: str, esim_cellular_id: str
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
        client.v1.feature_profile.mobility.global_.esimcellular.delete_esim_cellular_profile_feature_for_mobility()


