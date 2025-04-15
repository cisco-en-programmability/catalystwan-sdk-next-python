=======================================
sdavc.protocol_pack.maintenance.upgrade
=======================================


Operation: POST /dataservice/sdavc/protocol-pack/maintenance/upgrade
--------------------------------------------------------------------


Deploy protocol pack to devices

.. code:: python

    def post(payload: ProtocolPackUpgradeRequest) -> None: ...


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
        client.sdavc.protocol_pack.maintenance.upgrade.post()


.. toctree::
    :maxdepth: 1

    cancel
    status
    models

