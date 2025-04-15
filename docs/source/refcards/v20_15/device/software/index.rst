===============
device.software
===============


Operation: GET /dataservice/device/software
-------------------------------------------


Get software list from device

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.device.software.get()


.. toctree::
    :maxdepth: 1

    synced

