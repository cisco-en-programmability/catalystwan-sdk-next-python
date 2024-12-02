===========
device.tloc
===========


Operation: GET /dataservice/device/tloc
---------------------------------------


Get TLOC status list

.. code:: python

    def get_device_tloc_status(
        device_id: Optional[str] = None, color: Optional[str] = None
    ) -> DeviceTlocDataWithBfd: ...


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
        client.device.tloc.get_device_tloc_status()


.. toctree::
    :maxdepth: 1

    models

