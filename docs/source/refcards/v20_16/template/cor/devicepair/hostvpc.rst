===============================
template.cor.devicepair.hostvpc
===============================


Operation: GET /dataservice/template/cor/devicepair/hostvpc
-----------------------------------------------------------


Deprecated!!!

Get host VPC details

.. code:: python

    def get(transit_vpc_id: str, device_pair_id: str) -> Any: ...


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
        client.template.cor.devicepair.hostvpc.get()


