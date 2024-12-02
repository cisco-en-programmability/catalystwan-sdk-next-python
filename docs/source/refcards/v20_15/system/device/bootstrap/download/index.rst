================================
system.device.bootstrap.download
================================


Operation: GET /dataservice/system/device/bootstrap/download/{id}
-----------------------------------------------------------------


Download vEdge device config

.. code:: python

    def get_bootstrap_config_zip(id: str) -> GetBootstrapConfigZip: ...


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
        client.system.device.bootstrap.download.get_bootstrap_config_zip()


.. toctree::
    :maxdepth: 1

    models

