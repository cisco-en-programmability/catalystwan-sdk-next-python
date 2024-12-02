==============================================
sdavc.protocol_pack.maintenance.upload.confirm
==============================================


Operation: POST /dataservice/sdavc/protocol-pack/maintenance/upload/confirm/{uuid}
----------------------------------------------------------------------------------


Confirm uploaded protocol pack

.. code:: python

    def confirm_protocol_pack_upload(uuid: str) -> None: ...


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
        client.sdavc.protocol_pack.maintenance.upload.confirm.confirm_protocol_pack_upload()


