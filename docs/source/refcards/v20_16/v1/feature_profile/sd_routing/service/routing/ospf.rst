==================================================
v1.feature_profile.sd_routing.service.routing.ospf
==================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf
------------------------------------------------------------------------------------------


Get all SD-Routing LAN OSPF features for service VRF from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_ospf_features(
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
        client.v1.feature_profile.sd_routing.service.routing.ospf.get_sdrouting_service_vrf_ospf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf
-------------------------------------------------------------------------------------------


Create a SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_ospf_feature(
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
        client.v1.feature_profile.sd_routing.service.routing.ospf.create_sdrouting_service_vrf_ospf_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------


Get the SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_ospf_feature(
        service_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.service.routing.ospf.get_sdrouting_service_vrf_ospf_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------


Edit the SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_ospf_feature(
        service_id: str, ospf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.routing.ospf.edit_sdrouting_service_vrf_ospf_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------


Delete the SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_ospf_feature(
        service_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.service.routing.ospf.delete_sdrouting_service_vrf_ospf_feature()


