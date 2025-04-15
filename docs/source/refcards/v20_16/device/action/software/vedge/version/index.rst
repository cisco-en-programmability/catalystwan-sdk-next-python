====================================
device.action.software.vedge.version
====================================


Operation: GET /dataservice/device/action/software/vedge/version
----------------------------------------------------------------


Get vEdge software version

.. code:: python

    def get() -> FindVEdgeSoftwareVersion: ...


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
        client.device.action.software.vedge.version.get()


.. toctree::
    :maxdepth: 1

    models

