===========
partner.vpn
===========


Operation: GET /dataservice/partner/vpn
---------------------------------------


Get all VPNs

.. code:: python

    def get_vpn_list() -> VpnListRes: ...


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
        client.partner.vpn.get_vpn_list()


.. toctree::
    :maxdepth: 1

    models

