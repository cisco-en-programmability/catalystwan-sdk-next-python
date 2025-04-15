===============================
system.device.bootstrap.devices
===============================


Operation: POST /dataservice/system/device/bootstrap/devices
------------------------------------------------------------


Create bootstrap config for software vEdges

.. code:: python

    def post(
        payload: VEdgeBootstrapConfig,
    ) -> GenerateBootstrapConfigForVedgesResponse: ...


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
        client.system.device.bootstrap.devices.post()


.. toctree::
    :maxdepth: 1

    models

