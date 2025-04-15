=======================================
system.device.bootstrap.generic.devices
=======================================


Operation: GET /dataservice/system/device/bootstrap/generic/devices
-------------------------------------------------------------------


Create bootstrap config for software vEdges

.. code:: python

    def get(
        wanif: Optional[str] = None,
        sd_routing_device: Optional[bool] = None,
    ) -> GenerateGenericBootstrapConfigForVedges: ...


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
        client.system.device.bootstrap.generic.devices.get()


.. toctree::
    :maxdepth: 1

    models

