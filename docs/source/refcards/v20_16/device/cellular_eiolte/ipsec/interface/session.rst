==============================================
device.cellular_eiolte.ipsec.interface.session
==============================================


Operation: GET /dataservice/device/cellularEiolte/ipsec/interface/session
-------------------------------------------------------------------------


Get cellular ipsec interface info from device

.. code:: python

    def get_aon_ipsec_interface_sessionnfo(device_id: str) -> Any: ...


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
        client.device.cellular_eiolte.ipsec.interface.session.get_aon_ipsec_interface_sessionnfo()


