=================
device.action.vpn
=================


Operation: GET /dataservice/device/action/vpn
---------------------------------------------


Create VPN list

.. code:: python

    def get() -> CreateVpnList: ...


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
        client.device.action.vpn.get()


.. toctree::
    :maxdepth: 1

    models

