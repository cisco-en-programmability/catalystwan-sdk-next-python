============================================
v1.feature_profile.sd_routing.system.logging
============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging
-----------------------------------------------------------------------------------


Get all SD-Routing Logging features from a specific system feature profile

.. code:: python

    def get_sdrouting_logging_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.logging.get_sdrouting_logging_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging
------------------------------------------------------------------------------------


Create a SD-Routing Logging feature from a specific system feature profile

.. code:: python

    def create_sdrouting_logging_feature(
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
        client.v1.feature_profile.sd_routing.system.logging.create_sdrouting_logging_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}
-----------------------------------------------------------------------------------------------


Get the SD-Routing Logging feature from a specific system feature profile

.. code:: python

    def get_sdrouting_logging_feature(
        system_id: str, logging_id: str
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
        client.v1.feature_profile.sd_routing.system.logging.get_sdrouting_logging_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}
-----------------------------------------------------------------------------------------------


Edit the SD-Routing Logging feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_logging_feature(
        system_id: str, logging_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.logging.edit_sdrouting_logging_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}
--------------------------------------------------------------------------------------------------


Delete the SD-Routing Logging feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_logging_feature(
        system_id: str, logging_id: str
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
        client.v1.feature_profile.sd_routing.system.logging.delete_sdrouting_logging_feature()


