===============
device.bfd.tloc
===============


Operation: GET /dataservice/device/bfd/tloc
-------------------------------------------


Get TLOC summary from device (Real Time)

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.bfd.tloc.get()


.. toctree::
    :maxdepth: 1

    detail/index

