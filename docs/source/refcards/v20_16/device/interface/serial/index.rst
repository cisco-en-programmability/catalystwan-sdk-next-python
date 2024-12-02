=======================
device.interface.serial
=======================


Operation: GET /dataservice/device/interface/serial
---------------------------------------------------


Get serial interface

.. code:: python

    def get_device_serial_interface(
        device_id: str,
        vpn_id: Optional[str] = None,
        ifname: Optional[IfnameParam] = None,
        af_type: Optional[AfTypeParam] = None,
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
        client.device.interface.serial.get_device_serial_interface()


.. toctree::
    :maxdepth: 1

    models

