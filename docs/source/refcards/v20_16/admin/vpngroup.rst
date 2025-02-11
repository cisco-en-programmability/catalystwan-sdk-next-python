==============
admin.vpngroup
==============


Operation: GET /dataservice/admin/vpngroup
------------------------------------------


Get VPN groups

.. code:: python

    def get_vpn_groups() -> List[Any]: ...


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
        client.admin.vpngroup.get_vpn_groups()


Operation: POST /dataservice/admin/vpngroup
-------------------------------------------


Add VPN group

.. code:: python

    def create_vpn_group(payload: Optional[Any] = None) -> None: ...


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
        client.admin.vpngroup.create_vpn_group()


Operation: PUT /dataservice/admin/vpngroup/{id}
-----------------------------------------------


Update VPN group

.. code:: python

    def edit_vpn_group(
        id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.admin.vpngroup.edit_vpn_group()


Operation: DELETE /dataservice/admin/vpngroup/{id}
--------------------------------------------------


Delete VPN group

.. code:: python

    def delete_vpn_group(id: str) -> None: ...


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
        client.admin.vpngroup.delete_vpn_group()


