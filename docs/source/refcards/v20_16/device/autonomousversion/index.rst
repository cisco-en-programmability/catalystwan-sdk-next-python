========================
device.autonomousversion
========================


Operation: GET /dataservice/device/autonomousversion
----------------------------------------------------


Get Software version from device

.. code:: python

    def get_autonomous_software_version(
        device_id: str,
    ) -> SoftwareVersion: ...


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
        client.device.autonomousversion.get_autonomous_software_version()


.. toctree::
    :maxdepth: 1

    models

