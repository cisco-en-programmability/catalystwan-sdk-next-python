======================================================
v1.feature_profile.sd_routing.transport.management_vrf
======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf
------------------------------------------------------------------------------------------------


Get all SD-Routing Management VRF features from a specific transport feature profile

.. code:: python

    def get_sdrouting_management_vrf_features(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.get_sdrouting_management_vrf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf
-------------------------------------------------------------------------------------------------


Create a SD-Routing Management VRF feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_management_vrf_feature(
        transport_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.create_sdrouting_management_vrf_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}
--------------------------------------------------------------------------------------------------------


Get the SD-Routing Management VRF feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_management_vrf_feature(
        transport_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.get_sdrouting_management_vrf_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}
--------------------------------------------------------------------------------------------------------


Edit the SD-Routing Management VRF feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_management_vrf_feature(
        transport_id: str, vrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.edit_sdrouting_management_vrf_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}
-----------------------------------------------------------------------------------------------------------


Delete the SD-Routing Management VRF feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_management_vrf_feature(
        transport_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.delete_sdrouting_management_vrf_feature()


.. toctree::
    :maxdepth: 1

    interface/index

