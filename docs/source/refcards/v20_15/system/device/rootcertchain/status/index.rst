==================================
system.device.rootcertchain.status
==================================


Operation: GET /dataservice/system/device/rootcertchain/status
--------------------------------------------------------------


Get controllers vEdge sync status

.. code:: python

    def get_root_cert_status_all(state: str) -> GetRootCertStatusAll: ...


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
        client.system.device.rootcertchain.status.get_root_cert_status_all()


.. toctree::
    :maxdepth: 1

    models

