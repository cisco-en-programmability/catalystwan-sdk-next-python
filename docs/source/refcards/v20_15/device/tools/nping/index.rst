==================
device.tools.nping
==================


Operation: POST /dataservice/device/tools/nping/{deviceIP}
----------------------------------------------------------


NPing device

.. code:: python

    def nping_device(
        device_ip: str, payload: Optional[NPingRequest] = None
    ) -> NPingResponse: ...


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
        client.device.tools.nping.nping_device()


.. toctree::
    :maxdepth: 1

    models

