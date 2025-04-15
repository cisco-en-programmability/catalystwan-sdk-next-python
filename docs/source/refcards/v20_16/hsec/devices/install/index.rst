====================
hsec.devices.install
====================


Operation: GET /dataservice/hsec/devices/install
------------------------------------------------


Retrieve list of devices which has HSEC fetched

.. code:: python

    def get() -> List[GetHsecDevicesPayloadInner]: ...


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
        client.hsec.devices.install.get()


.. toctree::
    :maxdepth: 1

    models

