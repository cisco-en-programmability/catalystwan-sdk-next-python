=====================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular
=====================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular
------------------------------------------------------------------------------------------------------------------------


Create a Global VRF Cellular interface Feature for transport feature profile

.. code:: python

    def post(transport_id: str, vrf_id: str, payload: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}
--------------------------------------------------------------------------------------------------------------------------------


Update a Global VRF Cellular Interface Feature for transport feature profile

.. code:: python

    def put(
        transport_id: str, vrf_id: str, intf_id: str, payload: str
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}
-----------------------------------------------------------------------------------------------------------------------------------


Delete a Global VRF Cellular interface Feature for transport feature profile

.. code:: python

    def delete(transport_id: str, vrf_id: str, intf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular
-----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str, vrf_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}
--------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str, vrf_id: str, intf_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.get()


.. toctree::
    :maxdepth: 1

    tracker/index
    trackergroup/index

