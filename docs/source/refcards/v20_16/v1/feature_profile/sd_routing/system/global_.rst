============================================
v1.feature_profile.sd_routing.system.global_
============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global
----------------------------------------------------------------------------------


Get all SD-Routing global setting features from a specific system feature profile

.. code:: python

    def get_sdrouting_global_setting_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.global_.get_sdrouting_global_setting_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global
-----------------------------------------------------------------------------------


Create a SD-Routing global setting feature from a specific system feature profile

.. code:: python

    def create_sdrouting_global_setting_feature(
        system_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.global_.create_sdrouting_global_setting_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}
---------------------------------------------------------------------------------------------


Get the SD-Routing global setting feature from a specific system feature profile

.. code:: python

    def get_sdrouting_global_setting_feature(
        system_id: str, global_id: str
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
        client.v1.feature_profile.sd_routing.system.global_.get_sdrouting_global_setting_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}
---------------------------------------------------------------------------------------------


Edit the SD-Routing global setting feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_global_setting_feature(
        system_id: str, global_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.global_.edit_sdrouting_global_setting_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}
------------------------------------------------------------------------------------------------


Delete the SD-Routing global setting feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_global_setting_feature(
        system_id: str, global_id: str
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
        client.v1.feature_profile.sd_routing.system.global_.delete_sdrouting_global_setting_feature()


