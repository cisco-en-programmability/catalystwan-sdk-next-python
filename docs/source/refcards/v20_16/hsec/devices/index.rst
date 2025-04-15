============
hsec.devices
============


Operation: GET /dataservice/hsec/devices
----------------------------------------


Retrieve list of devices which are valid for fetch of HSEC license

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
        client.hsec.devices.get()


.. toctree::
    :maxdepth: 1

    install/index
    models

