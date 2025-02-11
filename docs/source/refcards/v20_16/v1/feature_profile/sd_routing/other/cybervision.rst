===============================================
v1.feature_profile.sd_routing.other.cybervision
===============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision
-------------------------------------------------------------------------------------


Get Cybervision Profile feature for Other feature profile

.. code:: python

    def get_cybervision_profile_feature_for_other(
        other_id: str,
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
        client.v1.feature_profile.sd_routing.other.cybervision.get_cybervision_profile_feature_for_other()


Operation: POST /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision
--------------------------------------------------------------------------------------


Create a Cybervision Profile feature for Other feature profile

.. code:: python

    def create_cybervision_profile_feature_for_other(
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
        client.v1.feature_profile.sd_routing.other.cybervision.create_cybervision_profile_feature_for_other()


Operation: GET /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}
-----------------------------------------------------------------------------------------------------


Get Cybervision Profile feature by FeatureId for Other feature profile

.. code:: python

    def get_cybervision_profile_feature_by_feature_id_for_other(
        other_id: str, cybervision_id: str
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
        client.v1.feature_profile.sd_routing.other.cybervision.get_cybervision_profile_feature_by_feature_id_for_other()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}
-----------------------------------------------------------------------------------------------------


Update a Cybervision Profile feature for Other feature profile

.. code:: python

    def edit_cybervision_profile_feature_for_other(
        other_id: str, cybervision_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.other.cybervision.edit_cybervision_profile_feature_for_other()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}
--------------------------------------------------------------------------------------------------------


Delete a Cybervision Profile feature for Other feature profile

.. code:: python

    def delete_cybervision_profile_feature_for_other(
        other_id: str, cybervision_id: str
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
        client.v1.feature_profile.sd_routing.other.cybervision.delete_cybervision_profile_feature_for_other()


