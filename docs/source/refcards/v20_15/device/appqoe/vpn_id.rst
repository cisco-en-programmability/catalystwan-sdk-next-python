====================
device.appqoe.vpn_id
====================


Operation: GET /dataservice/device/appqoe/vpn-id
------------------------------------------------


Get Appqoe Active vpn Id details from device

.. code:: python

    def create_appqoe_vpn_id_list(
        vpn_id: str,
        device_id: str,
        client_ip: Optional[str] = None,
        server_ip: Optional[str] = None,
        server_port: Optional[str] = None,
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
        client.device.appqoe.vpn_id.create_appqoe_vpn_id_list()


