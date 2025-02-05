===========================
device.action.uniquevpnlist
===========================


Operation: POST /dataservice/device/action/uniquevpnlist
--------------------------------------------------------


Create unique VPN list

.. code:: python

    def create_unique_vpn_list(
        payload: Optional[Any] = None,
    ) -> List[Any]: ...


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
        client.device.action.uniquevpnlist.create_unique_vpn_list()


