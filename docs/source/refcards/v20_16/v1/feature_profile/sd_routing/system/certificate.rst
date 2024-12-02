================================================
v1.feature_profile.sd_routing.system.certificate
================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate
---------------------------------------------------------------------------------------


Get all SD-Routing certificate features from a specific system feature profile

.. code:: python

    def get_sdrouting_certificate_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.certificate.get_sdrouting_certificate_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate
----------------------------------------------------------------------------------------


Create a SD-Routing certificate feature from a specific system feature profile

.. code:: python

    def create_sdrouting_certificate_feature(
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
        client.v1.feature_profile.sd_routing.system.certificate.create_sdrouting_certificate_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate/{certificateId}
-------------------------------------------------------------------------------------------------------


Get the SD-Routing certificate feature from a specific system feature profile

.. code:: python

    def get_sdrouting_certificate_feature(
        system_id: str, certificate_id: str
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
        client.v1.feature_profile.sd_routing.system.certificate.get_sdrouting_certificate_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate/{certificateId}
-------------------------------------------------------------------------------------------------------


Edit the SD-Routing certificate feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_certificate_feature(
        system_id: str, certificate_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.system.certificate.edit_sdrouting_certificate_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate/{certificateId}
----------------------------------------------------------------------------------------------------------


Delete the SD-Routing certificate feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_certificate_feature(
        system_id: str, certificate_id: str
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
        client.v1.feature_profile.sd_routing.system.certificate.delete_sdrouting_certificate_feature()


