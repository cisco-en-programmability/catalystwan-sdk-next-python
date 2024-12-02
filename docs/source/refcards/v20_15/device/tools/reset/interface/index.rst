============================
device.tools.reset.interface
============================


Operation: POST /dataservice/device/tools/reset/interface/{deviceIP}
--------------------------------------------------------------------


Reset device interface

.. code:: python

    def process_interface_reset(
        device_ip: str, payload: Optional[ResetInterfaceReq] = None
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
        client.device.tools.reset.interface.process_interface_reset()


.. toctree::
    :maxdepth: 1

    models

