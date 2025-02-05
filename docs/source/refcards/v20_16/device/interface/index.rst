================
device.interface
================


Operation: GET /dataservice/device/interface
--------------------------------------------


Get device interfaces

.. code:: python

    def get_device_interface(
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
        client.device.interface.get_device_interface()


.. toctree::
    :maxdepth: 1

    arp_stats/index
    error_stats/index
    ipv6_stats/index
    pkt_size/index
    port_stats/index
    qos_stats/index
    queue_stats/index
    serial/index
    stats/index
    synced/index
    trustsec
    vpn
    models

