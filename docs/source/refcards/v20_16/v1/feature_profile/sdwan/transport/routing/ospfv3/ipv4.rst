======================================================
v1.feature_profile.sdwan.transport.routing.ospfv3.ipv4
======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv4
------------------------------------------------------------------------------------------------


Get all routing OSPFv3 IPv4 address family profile parcels for transport feature profile

.. code:: python

    def get_routing_ospfv3_ipv4_af_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv4.get_routing_ospfv3_ipv4_af_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------


Create a routing OSPFv3 IPv4 address family profile parcel for transport feature profile

.. code:: python

    def create_routing_ospfv3_ipv4_af_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv4.create_routing_ospfv3_ipv4_af_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------


Get the routing OSPFv3 IPv4 address family profile parcel by ID for transport feature profile

.. code:: python

    def get_routing_ospfv3_ipv4_af_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv4.get_routing_ospfv3_ipv4_af_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------


Update a routing OSPFv3 IPv4 address family profile parcel for transport feature profile

.. code:: python

    def edit_routing_ospfv3_ipv4_af_profile_parcel_for_transport(
        transport_id: str, ospfv3_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv4.edit_routing_ospfv3_ipv4_af_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv4/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------


Delete the routing OSPFv3 IPv4 address family profile parcel by ID for transport feature profile

.. code:: python

    def delete_routing_ospfv3_ipv4_af_profile_parcel_for_transport(
        transport_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv4.delete_routing_ospfv3_ipv4_af_profile_parcel_for_transport()


