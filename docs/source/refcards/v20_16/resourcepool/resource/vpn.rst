=========================
resourcepool.resource.vpn
=========================


Operation: GET /dataservice/resourcepool/resource/vpn
-----------------------------------------------------


Get tenant device vpn resource

.. code:: python

    def get_resources(tenant_id: str, tenant_vpn: int) -> Any: ...


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
        client.resourcepool.resource.vpn.get_resources()


Operation: PUT /dataservice/resourcepool/resource/vpn
-----------------------------------------------------


Create Vpn resource pool and return tenant device vpn

.. code:: python

    def create_resources(payload: Optional[Any] = None) -> Any: ...


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
        client.resourcepool.resource.vpn.create_resources()


Operation: DELETE /dataservice/resourcepool/resource/vpn
--------------------------------------------------------


Delete tenant device vpn and release the resource

.. code:: python

    def delete_resources(tenant_id: str, tenant_vpn: int) -> None: ...


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
        client.resourcepool.resource.vpn.delete_resources()


