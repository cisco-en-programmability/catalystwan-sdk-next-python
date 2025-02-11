==========================
device.interface.arp_stats
==========================


Operation: GET /dataservice/device/interface/arp_stats
------------------------------------------------------


Get interface ARP statistics

.. code:: python

    def get_device_interface_arp_stats(
        device_id: str,
        vpn_id: Optional[str] = None,
        ifname: Optional[IfnameParam] = None,
        af_type: Optional[AfTypeParam] = None,
    ) -> Any: ...


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
        client.device.interface.arp_stats.get_device_interface_arp_stats()


.. toctree::
    :maxdepth: 1

    models

