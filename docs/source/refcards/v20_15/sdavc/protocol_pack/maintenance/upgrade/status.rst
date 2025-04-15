==============================================
sdavc.protocol_pack.maintenance.upgrade.status
==============================================


Operation: GET /dataservice/sdavc/protocol-pack/maintenance/upgrade/status
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get() -> None: ...


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
        client.sdavc.protocol_pack.maintenance.upgrade.status.get()


Operation: GET /dataservice/sdavc/protocol-pack/maintenance/upgrade/status/{uuid}
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(uuid: str) -> None: ...


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
        client.sdavc.protocol_pack.maintenance.upgrade.status.get()


