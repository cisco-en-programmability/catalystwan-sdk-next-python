========================
device.bfd.sites.summary
========================


Operation: GET /dataservice/device/bfd/sites/summary
----------------------------------------------------


Get BFD site summary

.. code:: python

    def get(
        vpn_id: List[Vpnid], is_cached: Optional[bool] = False
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
        client.device.bfd.sites.summary.get()


.. toctree::
    :maxdepth: 1

    models

