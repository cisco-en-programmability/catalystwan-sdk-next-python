=============================================
sdavc.protocol_pack.maintenance.upload.status
=============================================


Operation: GET /dataservice/sdavc/protocol-pack/maintenance/upload/status/{uuid}
--------------------------------------------------------------------------------


Get protocol pack upload status

.. code:: python

    def get_protocol_pack_upload_status(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.maintenance.upload.status.get_protocol_pack_upload_status()


