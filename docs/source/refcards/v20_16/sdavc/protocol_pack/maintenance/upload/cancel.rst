=============================================
sdavc.protocol_pack.maintenance.upload.cancel
=============================================


Operation: POST /dataservice/sdavc/protocol-pack/maintenance/upload/cancel/{uuid}
---------------------------------------------------------------------------------


Cancel or discard an uploaded protocol pack

.. code:: python

    def cancel_protocol_pack_upload(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.maintenance.upload.cancel.cancel_protocol_pack_upload()


