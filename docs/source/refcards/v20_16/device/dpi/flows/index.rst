================
device.dpi.flows
================


Operation: GET /dataservice/device/dpi/flows
--------------------------------------------


Get DPI flow list from device (Real Time)

.. code:: python

    def create_dpi_flows_list(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        src_ip: Optional[str] = None,
        application: Optional[str] = None,
        family: Optional[str] = None,
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
        client.device.dpi.flows.create_dpi_flows_list()


.. toctree::
    :maxdepth: 1

    models

