==============================
partner.dnac.sda.netconfconfig
==============================


Operation: POST /dataservice/partner/dnac/sda/netconfconfig/{partnerId}
-----------------------------------------------------------------------


Create SDA enabled device from Netconf

.. code:: python

    def create_sda_config_from_netconf(
        partner_id: str, payload: SdaConfigRequest
    ) -> SdaDeviceConfigRes: ...


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
        client.partner.dnac.sda.netconfconfig.create_sda_config_from_netconf()


.. toctree::
    :maxdepth: 1

    models

