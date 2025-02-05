==========================
device.omp.mcastroutesadvt
==========================


Operation: GET /dataservice/device/omp/mcastroutesadvt
------------------------------------------------------


Get OMP multicast routes advertised list

.. code:: python

    def create_omp_mcast_routes_advt(device_id: str) -> List[Any]: ...


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
        client.device.omp.mcastroutesadvt.create_omp_mcast_routes_advt()


