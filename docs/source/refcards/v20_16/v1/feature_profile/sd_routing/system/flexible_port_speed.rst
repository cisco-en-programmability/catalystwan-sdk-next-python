========================================================
v1.feature_profile.sd_routing.system.flexible_port_speed
========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed
-----------------------------------------------------------------------------------------------


Get all SD-Routing flexible port speed features from a specific system feature profile

.. code:: python

    def get_sdrouting_flexible_port_speed_features(
        system_id: str,
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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.get_sdrouting_flexible_port_speed_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed
------------------------------------------------------------------------------------------------


Create a SD-Routing flexible port speed feature from a specific system feature profile

.. code:: python

    def create_sdrouting_flexible_port_speed_feature(
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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.create_sdrouting_flexible_port_speed_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed/{flexiblePortSpeedId}
---------------------------------------------------------------------------------------------------------------------


Get the SD-Routing flexible port speed feature from a specific system feature profile

.. code:: python

    def get_sdrouting_flexible_port_speed_feature(
        system_id: str, flexible_port_speed_id: str
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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.get_sdrouting_flexible_port_speed_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed/{flexiblePortSpeedId}
---------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing flexible port speed feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_flexible_port_speed_feature(
        system_id: str,
        flexible_port_speed_id: str,
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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.edit_sdrouting_flexible_port_speed_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed/{flexiblePortSpeedId}
------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing flexible port speed feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_flexible_port_speed_feature(
        system_id: str, flexible_port_speed_id: str
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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.delete_sdrouting_flexible_port_speed_feature()


