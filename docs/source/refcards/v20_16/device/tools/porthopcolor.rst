=========================
device.tools.porthopcolor
=========================


Operation: POST /dataservice/device/tools/porthopcolor/{deviceIP}
-----------------------------------------------------------------


Request port hop color

.. code:: python

    def process_port_hop_color(
        device_ip: str, payload: Optional[Any] = None
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
        client.device.tools.porthopcolor.process_port_hop_color()


