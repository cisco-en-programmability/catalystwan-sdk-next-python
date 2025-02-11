===========================================
v1.feature_profile.sd_routing.system.banner
===========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner
----------------------------------------------------------------------------------


Get all SD-Routing banner features from a specific system feature profile

.. code:: python

    def get_sdrouting_banner_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.banner.get_sdrouting_banner_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner
-----------------------------------------------------------------------------------


Create a SD-Routing banner feature from a specific system feature profile

.. code:: python

    def create_sdrouting_banner_feature(
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
        client.v1.feature_profile.sd_routing.system.banner.create_sdrouting_banner_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}
---------------------------------------------------------------------------------------------


Get the SD-Routing banner feature from a specific system feature profile

.. code:: python

    def get_sdrouting_banner_feature(
        system_id: str, banner_id: str
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
        client.v1.feature_profile.sd_routing.system.banner.get_sdrouting_banner_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}
---------------------------------------------------------------------------------------------


Edit the SD-Routing banner feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_banner_feature(
        system_id: str, banner_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.banner.edit_sdrouting_banner_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}
------------------------------------------------------------------------------------------------


Delete the SD-Routing banner feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_banner_feature(
        system_id: str, banner_id: str
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
        client.v1.feature_profile.sd_routing.system.banner.delete_sdrouting_banner_feature()


