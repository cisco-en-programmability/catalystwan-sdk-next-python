==============================================
sdavc.protocol_pack.maintenance.upgrade.cancel
==============================================


Operation: POST /dataservice/sdavc/protocol-pack/maintenance/upgrade/cancel
---------------------------------------------------------------------------


Cancel a Scheduled Deploy protocol pack job

.. code:: python

    def post() -> Any: ...


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
        client.sdavc.protocol_pack.maintenance.upgrade.cancel.post()


