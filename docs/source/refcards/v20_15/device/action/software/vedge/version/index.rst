====================================
device.action.software.vedge.version
====================================


Operation: GET /dataservice/device/action/software/vedge/version
----------------------------------------------------------------


Get vEdge software version

.. code:: python

    def find_v_edge_software_version() -> FindVEdgeSoftwareVersion: ...


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
        client.device.action.software.vedge.version.find_v_edge_software_version()


.. toctree::
    :maxdepth: 1

    models

