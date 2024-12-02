====================
device.pppoe.session
====================


Operation: GET /dataservice/device/pppoe/session
------------------------------------------------


Get PPPoE session list from device

.. code:: python

    def create_pp_po_e_interface_list(device_id: DeviceIp) -> Any: ...


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
        client.device.pppoe.session.create_pp_po_e_interface_list()


.. toctree::
    :maxdepth: 1

    models

