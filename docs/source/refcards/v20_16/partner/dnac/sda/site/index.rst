=====================
partner.dnac.sda.site
=====================


Operation: GET /dataservice/partner/dnac/sda/site/{partnerId}
-------------------------------------------------------------


Get SDA Sites for Partner

.. code:: python

    def get_sites_for_partner(partner_id: str) -> SdaSitesRes: ...


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
        client.partner.dnac.sda.site.get_sites_for_partner()


.. toctree::
    :maxdepth: 1

    models

