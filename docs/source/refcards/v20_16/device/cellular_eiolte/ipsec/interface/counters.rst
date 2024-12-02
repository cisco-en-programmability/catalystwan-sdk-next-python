===============================================
device.cellular_eiolte.ipsec.interface.counters
===============================================


Operation: GET /dataservice/device/cellularEiolte/ipsec/interface/counters
--------------------------------------------------------------------------


Get cellular ipsec interface info from device

.. code:: python

    def get_aon_ipsec_interface_counters_info(device_id: str) -> Any: ...


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
        client.device.cellular_eiolte.ipsec.interface.counters.get_aon_ipsec_interface_counters_info()


