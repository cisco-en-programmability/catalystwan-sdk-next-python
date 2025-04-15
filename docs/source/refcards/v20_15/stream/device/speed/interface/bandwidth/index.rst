=======================================
stream.device.speed.interface.bandwidth
=======================================


Operation: GET /dataservice/stream/device/speed/interface/bandwidth
-------------------------------------------------------------------


.. code:: python

    def get(
        device_uuid: DeviceUuid,
        circuit: Optional[str] = None,
        source_interface: Optional[str] = None,
    ) -> SpeedTestInterfaceResponse: ...


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
        client.stream.device.speed.interface.bandwidth.get()


.. toctree::
    :maxdepth: 1

    models

