================
device.reachable
================


Operation: GET /dataservice/device/reachable
--------------------------------------------


Get list of reachable devices

.. code:: python

    def get() -> DeviceReachableData: ...


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
        client.device.reachable.get()


.. toctree::
    :maxdepth: 1

    models

