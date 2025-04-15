=========================
device.interface.pkt_size
=========================


Operation: GET /dataservice/device/interface/pkt_size
-----------------------------------------------------


Get interface packet size

.. code:: python

    def get(
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
        client.device.interface.pkt_size.get()


.. toctree::
    :maxdepth: 1

    models

