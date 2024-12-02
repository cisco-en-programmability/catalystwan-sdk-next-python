============================
device.interface.error_stats
============================


Operation: GET /dataservice/device/interface/error_stats
--------------------------------------------------------


Get interface error stats

.. code:: python

    def get_device_interface_error_stats(
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
        client.device.interface.error_stats.get_device_interface_error_stats()


.. toctree::
    :maxdepth: 1

    models

