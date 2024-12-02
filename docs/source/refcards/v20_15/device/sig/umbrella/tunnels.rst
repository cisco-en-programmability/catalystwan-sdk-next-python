===========================
device.sig.umbrella.tunnels
===========================


Operation: GET /dataservice/device/sig/umbrella/tunnels
-------------------------------------------------------


Get SIG Umbrella tunnels from device

.. code:: python

    def get_sig_umbrella_tunnels(device_id: str) -> Any: ...


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
        client.device.sig.umbrella.tunnels.get_sig_umbrella_tunnels()


