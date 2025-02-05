====================================
v1.feature_profile.sd_routing.system
====================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system
----------------------------------------------------------------


Get all SD-Routing System Feature Profiles

.. code:: python

    def get_sdrouting_system_feature_profiles(
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
        client.v1.feature_profile.sd_routing.system.get_sdrouting_system_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system
-----------------------------------------------------------------


Create a SD-Routing System Feature Profile

.. code:: python

    def create_sdrouting_system_feature_profile(
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
        client.v1.feature_profile.sd_routing.system.create_sdrouting_system_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}
---------------------------------------------------------------------------


Get a SD-Routing System Feature Profile

.. code:: python

    def get_sdrouting_system_feature_profile(system_id: str) -> Any: ...


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
        client.v1.feature_profile.sd_routing.system.get_sdrouting_system_feature_profile()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}
---------------------------------------------------------------------------


Edit a SD-Routing System Feature Profile

.. code:: python

    def edit_sdrouting_system_feature_profile(
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
        client.v1.feature_profile.sd_routing.system.edit_sdrouting_system_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}
------------------------------------------------------------------------------


Delete a SD-Routing System Feature Profile

.. code:: python

    def delete_sdrouting_system_feature_profile(
        system_id: str,
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
        client.v1.feature_profile.sd_routing.system.delete_sdrouting_system_feature_profile()


.. toctree::
    :maxdepth: 1

    aaa
    banner
    certificate
    flexible_port_speed
    global_
    logging
    ntp
    snmp

