=========================================
v1.feature_profile.sd_routing.service.vrf
=========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf
---------------------------------------------------------------------------------


Get all SD-Routing VRF features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_features(service_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.get_sdrouting_service_vrf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf
----------------------------------------------------------------------------------


Create a SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_feature(
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
        client.v1.feature_profile.sd_routing.service.vrf.create_sdrouting_service_vrf_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}
-----------------------------------------------------------------------------------------


Get the SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_feature(
        service_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.get_sdrouting_service_vrf_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}
-----------------------------------------------------------------------------------------


Edit the SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_feature(
        service_id: str, vrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.vrf.edit_sdrouting_service_vrf_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}
--------------------------------------------------------------------------------------------


Delete the SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_feature(
        service_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.delete_sdrouting_service_vrf_feature()


.. toctree::
    :maxdepth: 1

    routing/index
    dmvpn_tunnel
    interface/index

