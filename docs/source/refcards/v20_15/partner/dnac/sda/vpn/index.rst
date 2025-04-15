====================
partner.dnac.sda.vpn
====================


Operation: GET /dataservice/partner/dnac/sda/vpn
------------------------------------------------


Get Overlay VPN list

.. code:: python

    def get() -> VpnListRes: ...


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
        client.partner.dnac.sda.vpn.get()


.. toctree::
    :maxdepth: 1

    models

