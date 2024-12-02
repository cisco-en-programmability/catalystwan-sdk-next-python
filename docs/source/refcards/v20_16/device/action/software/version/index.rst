==============================
device.action.software.version
==============================


Operation: GET /dataservice/device/action/software/version
----------------------------------------------------------


Get software version

.. code:: python

    def find_software_version() -> FindSoftwareVersion: ...


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
        client.device.action.software.version.find_software_version()


.. toctree::
    :maxdepth: 1

    models

