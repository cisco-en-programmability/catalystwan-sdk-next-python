==================
device.bfd.summary
==================


Operation: GET /dataservice/device/bfd/summary
----------------------------------------------


Get BFD summary from device (Real Time)

.. code:: python

    def create_bfd_summary(device_id: str) -> Any: ...


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
        client.device.bfd.summary.create_bfd_summary()


.. toctree::
    :maxdepth: 1

    device

