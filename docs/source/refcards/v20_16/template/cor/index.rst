============
template.cor
============


Operation: GET /dataservice/template/cor
----------------------------------------


Deprecated!!!

Get Cloud On Ramp list

.. code:: python

    def get() -> List[Any]: ...


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
        client.template.cor.get()


Operation: POST /dataservice/template/cor
-----------------------------------------


Deprecated!!!

Map Host to Transit VPC/VNet

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.cor.post()


.. toctree::
    :maxdepth: 1

    accountid
    acquire_resource_pool
    ami
    cloud/index
    create_resource_pool
    delete_devicepair
    device
    devicepair/index
    external_id
    get_transit_device_pair_and_host_list
    get_transit_vpn_list
    hostvpc
    map
    pem
    scale/index
    transitvpc/index

