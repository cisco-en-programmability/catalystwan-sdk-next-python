========================
device.cloudx.localexits
========================


Operation: GET /dataservice/device/cloudx/localexits
----------------------------------------------------


Get list of cloudexpress local exits from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        application: Optional[str] = None,
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
        client.device.cloudx.localexits.get()


.. toctree::
    :maxdepth: 1

    models

