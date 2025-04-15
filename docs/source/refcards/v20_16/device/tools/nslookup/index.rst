=====================
device.tools.nslookup
=====================


Operation: GET /dataservice/device/tools/nslookup
-------------------------------------------------


Get device tool nslookup

.. code:: python

    def get(vpn: VpnParam, dns: str, device_id: str) -> Any: ...


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
        client.device.tools.nslookup.get()


.. toctree::
    :maxdepth: 1

    models

