==================
device.license.pak
==================


Operation: GET /dataservice/device/license/pak
----------------------------------------------


Get license pak info from device

.. code:: python

    def get_license_pak_info(device_id: str) -> Any: ...


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
        client.device.license.pak.get_license_pak_info()


