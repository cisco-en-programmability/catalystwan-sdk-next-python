=======================================================
v1.feature_profile.sd_routing.service.vrf.routing.eigrp
=======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp
-----------------------------------------------------------------------------------------------


Get all SD-Routing VRF EIGRP features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_eigrp_features(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get_sdrouting_service_vrf_eigrp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp
------------------------------------------------------------------------------------------------


Create a SD-Routing VRF EIGRP feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_eigrp_feature(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.create_sdrouting_service_vrf_eigrp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}
---------------------------------------------------------------------------------------------------------


Get the SD-Routing VRF EIGRP feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_eigrp_feature(
        service_id: str, eigrp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get_sdrouting_service_vrf_eigrp_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}
---------------------------------------------------------------------------------------------------------


Edit the SD-Routing VRF EIGRP feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_eigrp_feature(
        service_id: str, eigrp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.edit_sdrouting_service_vrf_eigrp_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}
------------------------------------------------------------------------------------------------------------


Delete the SD-Routing VRF EIGRP feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_eigrp_feature(
        service_id: str, eigrp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.delete_sdrouting_service_vrf_eigrp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp
-------------------------------------------------------------------------------------------------------


Get the LAN VRF associated EIGRP Features for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_eigrp_features(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get_service_vrf_associated_routing_eigrp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp
--------------------------------------------------------------------------------------------------------


Associate a EIGRP feature with the LAN VRF feature for service feature profile

.. code:: python

    def create_service_vrf_and_routing_eigrp_feature_association(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.create_service_vrf_and_routing_eigrp_feature_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}
-----------------------------------------------------------------------------------------------------------------


Get the LAN VRF associated EIGRP feature by ID for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_eigrp_feature_by_feature_id(
        service_id: str, vrf_id: str, eigrp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get_service_vrf_associated_routing_eigrp_feature_by_feature_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}
-----------------------------------------------------------------------------------------------------------------


Replace the EIGRP feature for LAN VRF feature in service feature profile

.. code:: python

    def edit_service_vrf_and_routing_eigrp_feature_association(
        service_id: str,
        vrf_id: str,
        eigrp_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.edit_service_vrf_and_routing_eigrp_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}
--------------------------------------------------------------------------------------------------------------------


Delete the LAN VRF feature and EIGRP feature association for service feature profile

.. code:: python

    def delete_service_vrf_and_routing_eigrp_association(
        service_id: str, vrf_id: str, eigrp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.delete_service_vrf_and_routing_eigrp_association()


