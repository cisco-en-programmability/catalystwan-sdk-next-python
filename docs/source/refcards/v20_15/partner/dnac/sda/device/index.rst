=======================
partner.dnac.sda.device
=======================


Operation: GET /dataservice/partner/dnac/sda/device/{partnerId}
---------------------------------------------------------------


.. code:: python

    @overload
    def get(partner_id: str) -> SdaDevicesRes: ...


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
        client.partner.dnac.sda.device.get()


Operation: GET /dataservice/partner/dnac/sda/device/{partnerId}/{uuid}
----------------------------------------------------------------------


.. code:: python

    @overload
    def get(partner_id: str, uuid: str) -> SdaDevicesRes: ...


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
        client.partner.dnac.sda.device.get()


.. toctree::
    :maxdepth: 1

    models

