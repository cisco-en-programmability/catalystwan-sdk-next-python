========================================
v1.feature_profile.sd_routing.system.ntp
========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp
-------------------------------------------------------------------------------


Get all SD-Routing NTP features from a specific system feature profile

.. code:: python

    def get_sdrouting_ntp_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.get_sdrouting_ntp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp
--------------------------------------------------------------------------------


Create a SD-Routing NTP feature from a specific system feature profile

.. code:: python

    def create_sdrouting_ntp_feature(
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
        client.v1.feature_profile.sd_routing.system.ntp.create_sdrouting_ntp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp/{ntpId}
---------------------------------------------------------------------------------------


Get the SD-Routing NTP feature from a specific system feature profile

.. code:: python

    def get_sdrouting_ntp_feature(system_id: str, ntp_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.get_sdrouting_ntp_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp/{ntpId}
---------------------------------------------------------------------------------------


Edit the SD-Routing NTP feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_ntp_feature(
        system_id: str, ntp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.ntp.edit_sdrouting_ntp_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp/{ntpId}
------------------------------------------------------------------------------------------


Delete the SD-Routing NTP feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_ntp_feature(
        system_id: str, ntp_id: str
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
        client.v1.feature_profile.sd_routing.system.ntp.delete_sdrouting_ntp_feature()


