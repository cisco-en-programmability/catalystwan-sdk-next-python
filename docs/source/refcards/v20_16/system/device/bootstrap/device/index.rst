==============================
system.device.bootstrap.device
==============================


Operation: GET /dataservice/system/device/bootstrap/device/{uuid}
-----------------------------------------------------------------


Create vEdge device config

.. code:: python

    def get(
        uuid: str,
        configtype: str,
        incl_def_root_cert: bool,
        version: Optional[str] = "v1",
        wanif: Optional[str] = None,
    ) -> GenerateBootstrapConfigForVedge: ...


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
        client.system.device.bootstrap.device.get()


.. toctree::
    :maxdepth: 1

    models

