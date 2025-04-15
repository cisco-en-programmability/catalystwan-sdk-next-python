=================================
device.redundancy_group.app_group
=================================


Operation: GET /dataservice/device/redundancy-group/app-group
-------------------------------------------------------------


Get Redundancy Group Information

.. code:: python

    def get(device_id: DeviceIp) -> None: ...


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
        client.device.redundancy_group.app_group.get()


.. toctree::
    :maxdepth: 1

    models

