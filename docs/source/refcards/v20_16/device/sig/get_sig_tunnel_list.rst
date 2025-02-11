==============================
device.sig.get_sig_tunnel_list
==============================


Operation: GET /dataservice/device/sig/getSigTunnelList
-------------------------------------------------------


get Sig TunnelList

.. code:: python

    def get_sig_tunnel_list(
        page_size: Optional[str] = None,
        offset: Optional[str] = None,
        last_n_hours: Optional[str] = None,
        site_id: Optional[str] = None,
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
        client.device.sig.get_sig_tunnel_list.get_sig_tunnel_list()


