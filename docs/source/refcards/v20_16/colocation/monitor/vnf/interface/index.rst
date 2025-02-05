================================
colocation.monitor.vnf.interface
================================


Operation: GET /dataservice/colocation/monitor/vnf/interface
------------------------------------------------------------


Deprecated!!!

Get interface detail of VNF

.. code:: python

    def get_vnf_interface_detail(
        vnf_name: str,
        device_ip: Optional[DeviceIp] = None,
        device_class: Optional[str] = None,
    ) -> None: ...


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
        client.colocation.monitor.vnf.interface.get_vnf_interface_detail()


.. toctree::
    :maxdepth: 1

    models

