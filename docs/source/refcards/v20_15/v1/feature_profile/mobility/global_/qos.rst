=======================================
v1.feature_profile.mobility.global_.qos
=======================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{globalId}/qos
-----------------------------------------------------------------------------


Get Qos Feature for Global feature profile

.. code:: python

    def get_qos_feature_for_global(global_id: str) -> str: ...


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
        client.v1.feature_profile.mobility.global_.qos.get_qos_feature_for_global()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{globalId}/qos
------------------------------------------------------------------------------


Create a Qos Feature for Global feature profile

.. code:: python

    def create_qos_feature_for_global(
        global_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.qos.create_qos_feature_for_global()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}
-------------------------------------------------------------------------------------


Get Qos Feature by parcelId for Global feature profile

.. code:: python

    def get_qos_feature_by_parcel_id_for_global(
        global_id: str, qos_id: str
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
        client.v1.feature_profile.mobility.global_.qos.get_qos_feature_by_parcel_id_for_global()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}
-------------------------------------------------------------------------------------


Update a Qos Feature for Global feature profile

.. code:: python

    def edit_qos_feature_for_global(
        global_id: str, qos_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.qos.edit_qos_feature_for_global()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}
----------------------------------------------------------------------------------------


Delete a Qos Feature for Global feature profile

.. code:: python

    def delete_qos_feature_for_global(
        global_id: str, qos_id: str
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
        client.v1.feature_profile.mobility.global_.qos.delete_qos_feature_for_global()


