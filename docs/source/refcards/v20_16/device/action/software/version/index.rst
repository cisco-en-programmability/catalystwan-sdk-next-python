==============================
device.action.software.version
==============================


Operation: GET /dataservice/device/action/software/version
----------------------------------------------------------


Get software version

.. code:: python

    def get() -> FindSoftwareVersion: ...


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
        client.device.action.software.version.get()


.. toctree::
    :maxdepth: 1

    models

