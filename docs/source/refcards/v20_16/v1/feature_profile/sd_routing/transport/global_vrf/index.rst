==================================================
v1.feature_profile.sd_routing.transport.global_vrf
==================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf
--------------------------------------------------------------------------------------------


Get all SD-Routing Global VRF features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_global_vrf_features(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.get_sdrouting_transport_global_vrf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf
---------------------------------------------------------------------------------------------


Create a SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_global_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.create_sdrouting_transport_global_vrf_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}
----------------------------------------------------------------------------------------------------


Get the SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_global_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.get_sdrouting_transport_global_vrf_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}
----------------------------------------------------------------------------------------------------


Edit the SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_global_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.edit_sdrouting_transport_global_vrf_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}
-------------------------------------------------------------------------------------------------------


Delete the SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_global_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.delete_sdrouting_transport_global_vrf_feature()


.. toctree::
    :maxdepth: 1

    routing/index
    interface/index
    multicloud_connection

