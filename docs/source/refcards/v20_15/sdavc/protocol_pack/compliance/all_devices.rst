==========================================
sdavc.protocol_pack.compliance.all_devices
==========================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/all-devices
----------------------------------------------------------------------


Get all device compliance details

.. code:: python

    def get_all_sdavc_device() -> None: ...


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
        client.sdavc.protocol_pack.compliance.all_devices.get_all_sdavc_device()


