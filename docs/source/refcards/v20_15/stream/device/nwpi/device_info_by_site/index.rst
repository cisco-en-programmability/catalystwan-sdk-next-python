======================================
stream.device.nwpi.device_info_by_site
======================================


Operation: GET /dataservice/stream/device/nwpi/deviceInfoBySite
---------------------------------------------------------------


Deprecated!!!

Get device and interface data by site

.. code:: python

    def get_devices_and_interfaces_by_site(
        site_id: str, mode: Optional[str] = None
    ) -> DeviceInfoResponsePayloadData: ...


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
        client.stream.device.nwpi.device_info_by_site.get_devices_and_interfaces_by_site()


.. toctree::
    :maxdepth: 1

    models

