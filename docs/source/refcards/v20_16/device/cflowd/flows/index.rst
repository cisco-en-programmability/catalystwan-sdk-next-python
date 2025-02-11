===================
device.cflowd.flows
===================


Operation: GET /dataservice/device/cflowd/flows
-----------------------------------------------


Get list of cflowd flows from device

.. code:: python

    def create_cflow_collector_list(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        src_ip: Optional[str] = None,
        dest_ip: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.device.cflowd.flows.create_cflow_collector_list()


.. toctree::
    :maxdepth: 1

    models

