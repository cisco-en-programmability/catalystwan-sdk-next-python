=========================================================
v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4
=========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------


Get all SD-Routing LAN OSPFv3 IPv4 features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_ospfv3_ipv4_features(
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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.get_sdrouting_service_vrf_ospfv3_ipv4_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4
--------------------------------------------------------------------------------------------------


Create a SD-Routing LAN OSPFv3 IPv4 feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_ospfv3_ipv4_feature(
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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.create_sdrouting_service_vrf_ospfv3_ipv4_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------


Get the SD-Routing LAN OSPFv3 IPv4 feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_ospfv3_ipv4_feature(
        service_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.get_sdrouting_service_vrf_ospfv3_ipv4_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------


Edit the SD-Routing LAN OSPFv3 IPv4 feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_ospfv3_ipv4_feature(
        service_id: str, ospfv3_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.edit_sdrouting_service_vrf_ospfv3_ipv4_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------


Delete the SD-Routing LAN OSPFv3 IPv4 feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_ospfv3_ipv4_feature(
        service_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.delete_sdrouting_service_vrf_ospfv3_ipv4_feature()


