===================
device.devicestatus
===================


Operation: GET /dataservice/device/devicestatus
-----------------------------------------------


Get devices status per type

.. code:: python

    def get() -> DeviceStatusData: ...


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
        client.device.devicestatus.get()


.. toctree::
    :maxdepth: 1

    models

