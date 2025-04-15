=========================
device.cflowd.flows_count
=========================


Operation: GET /dataservice/device/cflowd/flows-count
-----------------------------------------------------


Get cflowd flow count from device

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        src_ip: Optional[str] = None,
        dest_ip: Optional[str] = None,
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
        client.device.cflowd.flows_count.get()


.. toctree::
    :maxdepth: 1

    models

