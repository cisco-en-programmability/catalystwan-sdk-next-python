===================================
v1.feature_profile.sdwan.other.ucse
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse
-------------------------------------------------------------------------


Get Ucse Profile feature for Other feature profile

.. code:: python

    def get_ucse_profile_feature_for_other(other_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.other.ucse.get_ucse_profile_feature_for_other()


Operation: POST /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse
--------------------------------------------------------------------------


Create a Ucse Profile feature for Other feature profile

.. code:: python

    def create_ucse_profile_feature_for_other(
        other_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.other.ucse.create_ucse_profile_feature_for_other()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}
----------------------------------------------------------------------------------


Get Ucse Profile feature by FeatureId for Other feature profile

.. code:: python

    def get_ucse_profile_feature_by_id_f_feature_for_other(
        other_id: str, ucse_id: str
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
        client.v1.feature_profile.sdwan.other.ucse.get_ucse_profile_feature_by_id_f_feature_for_other()


Operation: PUT /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}
----------------------------------------------------------------------------------


Update a Ucse Profile feature for Other feature profile

.. code:: python

    def edit_ucse_profile_feature_for_other(
        other_id: str, ucse_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.other.ucse.edit_ucse_profile_feature_for_other()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}
-------------------------------------------------------------------------------------


Delete a Ucse Profile feature for Other feature profile

.. code:: python

    def delete_ucse_profile_feature_for_other(
        other_id: str, ucse_id: str
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
        client.v1.feature_profile.sdwan.other.ucse.delete_ucse_profile_feature_for_other()


