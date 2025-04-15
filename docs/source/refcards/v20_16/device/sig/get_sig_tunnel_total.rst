===============================
device.sig.get_sig_tunnel_total
===============================


Operation: GET /dataservice/device/sig/getSigTunnelTotal
--------------------------------------------------------


get Sig Tunnel Total coount

.. code:: python

    def get() -> Any: ...


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
        client.device.sig.get_sig_tunnel_total.get()


