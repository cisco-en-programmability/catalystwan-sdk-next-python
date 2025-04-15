=========================
resourcepool.resource.vpn
=========================


Operation: GET /dataservice/resourcepool/resource/vpn
-----------------------------------------------------


Get tenant device vpn resource

.. code:: python

    def get(tenant_id: str, tenant_vpn: int) -> Any: ...


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
        client.resourcepool.resource.vpn.get()


Operation: PUT /dataservice/resourcepool/resource/vpn
-----------------------------------------------------


Create Vpn resource pool and return tenant device vpn

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.resourcepool.resource.vpn.put()


Operation: DELETE /dataservice/resourcepool/resource/vpn
--------------------------------------------------------


Delete tenant device vpn and release the resource

.. code:: python

    def delete(tenant_id: str, tenant_vpn: int) -> None: ...


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
        client.resourcepool.resource.vpn.delete()


