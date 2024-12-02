========================================================================
v1.feature_profile.sd_routing.transport.global_vrf.multicloud_connection
========================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/multicloud-connection
---------------------------------------------------------------------------------------------------------------------------


Associate a Global VRF parcel with a Multicloud Connection Parcel for transport feature profile

.. code:: python

    def create_transport_global_vrf_and_multicloud_connection_parcel_association(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.multicloud_connection.create_transport_global_vrf_and_multicloud_connection_parcel_association()


