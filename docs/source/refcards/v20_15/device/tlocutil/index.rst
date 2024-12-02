===============
device.tlocutil
===============


Operation: GET /dataservice/device/tlocutil
-------------------------------------------


Get TLOC list

.. code:: python

    def get_device_tloc_util(site_id: Optional[str] = None) -> Any: ...


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
        client.device.tlocutil.get_device_tloc_util()


.. toctree::
    :maxdepth: 1

    detail

