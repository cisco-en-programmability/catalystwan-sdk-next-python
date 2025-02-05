================================
v1.feature_profile.sdwan.service
================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service
------------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_service_feature_profiles(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        details: Optional[bool] = False,
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.service.get_sdwan_service_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/service
-------------------------------------------------------------


Create a SDWAN Service Feature Profile

.. code:: python

    def create_sdwan_service_feature_profile(
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
        client.v1.feature_profile.sdwan.service.create_sdwan_service_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}
------------------------------------------------------------------------


Get a SDWAN Service Feature Profile with serviceId

.. code:: python

    def get_sdwan_service_feature_profile_by_profile_id(
        service_id: str, details: Optional[bool] = False
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.service.get_sdwan_service_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}
------------------------------------------------------------------------


Edit a SDWAN Service Feature Profile

.. code:: python

    def edit_sdwan_service_feature_profile(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.edit_sdwan_service_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}
---------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_service_feature_profile(service_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.delete_sdwan_service_feature_profile()


.. toctree::
    :maxdepth: 1

    dhcp_server/index
    lan/index
    routing/index
    switchport/index
    tracker/index
    trackergroup/index
    wirelesslan/index
    appqoe

