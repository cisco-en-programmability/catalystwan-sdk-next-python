============================
device.tunnel.gre_keepalives
============================


Operation: GET /dataservice/device/tunnel/gre-keepalives
--------------------------------------------------------


Get GRE keep alive information

.. code:: python

    def create_gre_keepalives_list(device_id: str) -> Any: ...


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
        client.device.tunnel.gre_keepalives.create_gre_keepalives_list()


