====================
v1.licensing.devices
====================


Operation: GET /dataservice/v1/licensing/devices
------------------------------------------------


Retrieve list of all devices along with license details if assigned

.. code:: python

    def get_msla_devices() -> DevicesDetails: ...


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
        client.v1.licensing.devices.get_msla_devices()


.. toctree::
    :maxdepth: 1

    models

