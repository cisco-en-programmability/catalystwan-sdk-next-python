==============================================
v1.feature_profile.sdwan.transport.routing.bgp
==============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp
----------------------------------------------------------------------------------------


Get Routing Bgp Profile Parcels for Transport feature profile

.. code:: python

    def get_routing_bgp_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.routing.bgp.get_routing_bgp_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp
-----------------------------------------------------------------------------------------


Create a Routing Bgp Profile Parcel for Transport feature profile

.. code:: python

    def create_routing_bgp_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.routing.bgp.create_routing_bgp_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------


Get Routing Bgp Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_routing_bgp_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, bgp_id: str
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
        client.v1.feature_profile.sdwan.transport.routing.bgp.get_routing_bgp_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------


Update a Routing Bgp Profile Parcel for Transport feature profile

.. code:: python

    def edit_routing_bgp_profile_parcel_for_transport(
        transport_id: str, bgp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.routing.bgp.edit_routing_bgp_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------


Delete a Routing Bgp Profile Parcel for Transport feature profile

.. code:: python

    def delete_routing_bgp_profile_parcel_for_transport(
        transport_id: str, bgp_id: str
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
        client.v1.feature_profile.sdwan.transport.routing.bgp.delete_routing_bgp_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

