===============================
system.device.bootstrap.devices
===============================


Operation: POST /dataservice/system/device/bootstrap/devices
------------------------------------------------------------


Create bootstrap config for software vEdges

.. code:: python

    def generate_bootstrap_config_for_vedges(
        payload: Optional[VEdgeBootstrapConfig] = None,
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
        client.system.device.bootstrap.devices.generate_bootstrap_config_for_vedges()


.. toctree::
    :maxdepth: 1

    models

