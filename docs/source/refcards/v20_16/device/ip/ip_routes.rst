===================
device.ip.ip_routes
===================


Operation: GET /dataservice/device/ip/ipRoutes
----------------------------------------------


Get ietf routing list from device

.. code:: python

    def create_ietf_routing_list(
        device_id: str,
        routing_instance_name: Optional[str] = None,
        address_family: Optional[str] = None,
        outgoing_interface: Optional[str] = None,
        source_protocol: Optional[str] = None,
        next_hop_address: Optional[str] = None,
    ) -> Any: ...


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
        client.device.ip.ip_routes.create_ietf_routing_list()


