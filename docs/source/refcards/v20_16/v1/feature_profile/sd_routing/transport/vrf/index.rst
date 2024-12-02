===========================================
v1.feature_profile.sd_routing.transport.vrf
===========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf
-------------------------------------------------------------------------------------


Get all SD-Routing VRF features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_vrf_features(
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
        client.v1.feature_profile.sd_routing.transport.vrf.get_sdrouting_transport_vrf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf
--------------------------------------------------------------------------------------


Create a SD-Routing VRF feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.vrf.create_sdrouting_transport_vrf_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}
---------------------------------------------------------------------------------------------


Get the SD-Routing VRF feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.vrf.get_sdrouting_transport_vrf_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}
---------------------------------------------------------------------------------------------


Edit the SD-Routing VRF feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.vrf.edit_sdrouting_transport_vrf_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}
------------------------------------------------------------------------------------------------


Delete the SD-Routing VRF feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_vrf_feature(
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
        client.v1.feature_profile.sd_routing.transport.vrf.delete_sdrouting_transport_vrf_feature()


.. toctree::
    :maxdepth: 1

    routing/index
    interface/index

