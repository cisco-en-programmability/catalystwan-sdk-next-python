=====================================
v1.feature_profile.sd_routing.service
=====================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service
-----------------------------------------------------------------


Get all SD-Routing Service Feature Profiles

.. code:: python

    def get_sd_routing_service_feature_profiles(
        offset: Optional[int] = None, limit: Optional[int] = 0
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
        client.v1.feature_profile.sd_routing.service.get_sd_routing_service_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service
------------------------------------------------------------------


Create a SD-Routing Service Feature Profile

.. code:: python

    def create_sd_routing_service_feature_profile(
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
        client.v1.feature_profile.sd_routing.service.create_sd_routing_service_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}
-----------------------------------------------------------------------------


Get a SD-Routing Service Feature Profile

.. code:: python

    def get_sd_routing_service_feature_profile(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.get_sd_routing_service_feature_profile()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}
-----------------------------------------------------------------------------


Edit a SD-Routing Service Feature Profile

.. code:: python

    def edit_sd_routing_service_feature_profile(
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
        client.v1.feature_profile.sd_routing.service.edit_sd_routing_service_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}
--------------------------------------------------------------------------------


Delete a SD-Routing Service Feature Profile

.. code:: python

    def delete_sd_routing_service_feature_profile(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.delete_sd_routing_service_feature_profile()


.. toctree::
    :maxdepth: 1

    multicloud_connection/index

