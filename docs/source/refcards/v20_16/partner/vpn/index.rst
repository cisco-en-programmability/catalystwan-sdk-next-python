===========
partner.vpn
===========


Operation: GET /dataservice/partner/vpn
---------------------------------------


Get all VPNs

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
        client.partner.vpn.get()


.. toctree::
    :maxdepth: 1

    models

