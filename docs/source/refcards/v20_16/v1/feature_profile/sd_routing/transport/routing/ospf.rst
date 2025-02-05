====================================================
v1.feature_profile.sd_routing.transport.routing.ospf
====================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf
----------------------------------------------------------------------------------------------


Get all SD-Routing WAN OSPF features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_routing_ospf_features(
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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.get_sdrouting_transport_routing_ospf_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf
-----------------------------------------------------------------------------------------------


Create a SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_routing_ospf_feature(
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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.create_sdrouting_transport_routing_ospf_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------------


Get the SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_routing_ospf_feature(
        transport_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.get_sdrouting_transport_routing_ospf_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------------


Edit the SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_routing_ospf_feature(
        transport_id: str, ospf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.edit_sdrouting_transport_routing_ospf_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------------------


Delete the SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_routing_ospf_feature(
        transport_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.delete_sdrouting_transport_routing_ospf_feature()


