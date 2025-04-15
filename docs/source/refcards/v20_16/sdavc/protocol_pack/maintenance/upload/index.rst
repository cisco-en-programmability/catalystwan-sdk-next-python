======================================
sdavc.protocol_pack.maintenance.upload
======================================


Operation: POST /dataservice/sdavc/protocol-pack/maintenance/upload
-------------------------------------------------------------------


Upload protocol pack to SDAVC

.. code:: python

    def post(payload: ProtocolPackUploadRequest) -> Any: ...


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
        client.sdavc.protocol_pack.maintenance.upload.post()


.. toctree::
    :maxdepth: 1

    cancel
    confirm
    status
    models

