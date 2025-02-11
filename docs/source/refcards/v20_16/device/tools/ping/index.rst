=================
device.tools.ping
=================


Operation: POST /dataservice/device/tools/ping/{deviceIP}
---------------------------------------------------------


Ping device

.. code:: python

    def ping_device(
        device_ip: str, payload: Optional[PingRequest] = None
    ) -> PingResponse: ...


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
        client.device.tools.ping.ping_device()


.. toctree::
    :maxdepth: 1

    models

