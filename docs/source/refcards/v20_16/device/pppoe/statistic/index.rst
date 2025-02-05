======================
device.pppoe.statistic
======================


Operation: GET /dataservice/device/pppoe/statistic
--------------------------------------------------


Get PPPoE statistics from device

.. code:: python

    def create_pp_po_e_neighbor_list(device_id: DeviceIp) -> Any: ...


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
        client.device.pppoe.statistic.create_pp_po_e_neighbor_list()


.. toctree::
    :maxdepth: 1

    models

