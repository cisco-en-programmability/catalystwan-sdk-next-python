================================
system.device.sync.rootcertchain
================================


Operation: GET /dataservice/system/device/sync/rootcertchain
------------------------------------------------------------


Sync root certificate

.. code:: python

    def sync_root_cert_chain() -> SyncRootCertChain: ...


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
        client.system.device.sync.rootcertchain.sync_root_cert_chain()


.. toctree::
    :maxdepth: 1

    models

