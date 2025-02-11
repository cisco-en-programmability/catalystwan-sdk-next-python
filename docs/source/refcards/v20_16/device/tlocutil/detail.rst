======================
device.tlocutil.detail
======================


Operation: GET /dataservice/device/tlocutil/detail
--------------------------------------------------


Get detailed TLOC list

.. code:: python

    def get_device_tloc_util_details(
        util: Optional[str] = None, site_id: Optional[str] = None
    ) -> Any: ...


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
        client.device.tlocutil.detail.get_device_tloc_util_details()


