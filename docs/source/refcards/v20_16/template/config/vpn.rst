===================
template.config.vpn
===================


Operation: GET /dataservice/template/config/vpn/{deviceId}
----------------------------------------------------------


Get list of configured VPN (excluding reserved VPN) for a device

.. code:: python

    def get_vpn_for_device(device_id: str) -> List[Any]: ...


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
        client.template.config.vpn.get_vpn_for_device()


