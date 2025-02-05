====================
partner.dnac.sda.vpn
====================


Operation: GET /dataservice/partner/dnac/sda/vpn
------------------------------------------------


Get Overlay VPN list

.. code:: python

    def get_overlay_vpn_list() -> VpnListRes: ...


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
        client.partner.dnac.sda.vpn.get_overlay_vpn_list()


.. toctree::
    :maxdepth: 1

    models

