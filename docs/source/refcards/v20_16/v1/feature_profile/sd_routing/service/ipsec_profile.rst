===================================================
v1.feature_profile.sd_routing.service.ipsec_profile
===================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile
-------------------------------------------------------------------------------------------


Get all SD-Routing IPSec profile features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_ipsec_profile_features(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.get_sdrouting_service_ipsec_profile_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile
--------------------------------------------------------------------------------------------


Create a SD-Routing IPSec profile feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_ipsec_profile_feature(
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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.create_sdrouting_service_ipsec_profile_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile/{ipsecProfileId}
------------------------------------------------------------------------------------------------------------


Get the SD-Routing IPSec profile feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_ipsec_profile_feature(
        service_id: str, ipsec_profile_id: str
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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.get_sdrouting_service_ipsec_profile_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile/{ipsecProfileId}
------------------------------------------------------------------------------------------------------------


Edit the SD-Routing IPSec profile feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_ipsec_profile_feature(
        service_id: str,
        ipsec_profile_id: str,
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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.edit_sdrouting_service_ipsec_profile_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile/{ipsecProfileId}
---------------------------------------------------------------------------------------------------------------


Delete the SD-Routing IPSec profile feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_ipsec_profile_feature(
        service_id: str, ipsec_profile_id: str
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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.delete_sdrouting_service_ipsec_profile_feature()


