=======================
partner.dnac.sda.device
=======================


Operation: GET /dataservice/partner/dnac/sda/device/{partnerId}
---------------------------------------------------------------


Get SDA enabled devices

.. code:: python

    def get_sda_enabled_devices(partner_id: str) -> SdaDevicesRes: ...


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
        client.partner.dnac.sda.device.get_sda_enabled_devices()


Operation: GET /dataservice/partner/dnac/sda/device/{partnerId}/{uuid}
----------------------------------------------------------------------


Get SDA enabled devices detail

.. code:: python

    def get_device_details(
        partner_id: str, uuid: str
    ) -> SdaDevicesRes: ...


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
        client.partner.dnac.sda.device.get_device_details()


.. toctree::
    :maxdepth: 1

    models

