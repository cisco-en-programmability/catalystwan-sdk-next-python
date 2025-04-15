========================
device.action.filter.vpn
========================


Operation: GET /dataservice/device/action/filter/vpn
----------------------------------------------------


Get filter VPN list

.. code:: python

    def get(
        site_id: Optional[str] = None, device_id: Optional[str] = None
    ) -> CreateFilterVpnList: ...


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
        client.device.action.filter.vpn.get()


.. toctree::
    :maxdepth: 1

    models

