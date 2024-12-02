============================
dca.template.policy.list.vpn
============================


Operation: POST /dataservice/dca/template/policy/list/vpn
---------------------------------------------------------


Get VPN details

.. code:: python

    def get_vpn_lists_dca(payload: Optional[Any] = None) -> List[Any]: ...


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
        client.dca.template.policy.list.vpn.get_vpn_lists_dca()


