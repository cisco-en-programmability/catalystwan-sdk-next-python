======================================================
v1.feature_profile.sd_routing.service.vrf.routing.ospf
======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf
------------------------------------------------------------------------------------------------------


Get the VRF associated OSPF features for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_ospf_features(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.get_service_vrf_associated_routing_ospf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf
-------------------------------------------------------------------------------------------------------


Associate an OSPF feature with the LAN VRF feature for service feature profile

.. code:: python

    def create_service_vrf_and_routing_ospf_parcel_association(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.create_service_vrf_and_routing_ospf_parcel_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------------------


Get the LAN VRF associated OSPF feature by ID for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_ospf_feature_by_id(
        service_id: str, vrf_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.get_service_vrf_associated_routing_ospf_feature_by_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------------------


Replace the OSPF feature for LAN VRF feature in service feature profile

.. code:: python

    def edit_service_vrf_and_routing_ospf_feature_association(
        service_id: str,
        vrf_id: str,
        ospf_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.edit_service_vrf_and_routing_ospf_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------------------


Delete the LAN VRF feature and OSPF feature association in service feature profile

.. code:: python

    def delete_service_vrf_and_routing_ospf_association(
        service_id: str, vrf_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.delete_service_vrf_and_routing_ospf_association()


