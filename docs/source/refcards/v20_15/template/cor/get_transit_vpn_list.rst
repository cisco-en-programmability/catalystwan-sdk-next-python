=================================
template.cor.get_transit_vpn_list
=================================


Operation: GET /dataservice/template/cor/getTransitVpnList
----------------------------------------------------------


Deprecated!!!

Get transit VPN list

.. code:: python

    def get(account_id: str) -> List[Any]: ...


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
        client.template.cor.get_transit_vpn_list.get()


