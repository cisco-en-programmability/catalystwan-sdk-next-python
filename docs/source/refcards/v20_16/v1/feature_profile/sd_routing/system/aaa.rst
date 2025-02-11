========================================
v1.feature_profile.sd_routing.system.aaa
========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa
-------------------------------------------------------------------------------


Get all SD-Routing AAA features from a specific system feature profile

.. code:: python

    def get_sdrouting_aaa_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.get_sdrouting_aaa_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa
--------------------------------------------------------------------------------


Create a SD-Routing AAA feature from a specific system feature profile

.. code:: python

    def create_sdrouting_aaa_feature(
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
        client.v1.feature_profile.sd_routing.system.aaa.create_sdrouting_aaa_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa/{aaaId}
---------------------------------------------------------------------------------------


Get the SD-Routing AAA feature from a specific system feature profile

.. code:: python

    def get_sdrouting_aaa_feature(system_id: str, aaa_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.get_sdrouting_aaa_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa/{aaaId}
---------------------------------------------------------------------------------------


Edit the SD-Routing AAA feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_aaa_feature(
        system_id: str, aaa_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.aaa.edit_sdrouting_aaa_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa/{aaaId}
------------------------------------------------------------------------------------------


Delete the SD-Routing AAA feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_aaa_feature(
        system_id: str, aaa_id: str
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
        client.v1.feature_profile.sd_routing.system.aaa.delete_sdrouting_aaa_feature()


