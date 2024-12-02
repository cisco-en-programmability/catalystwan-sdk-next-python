==========================
device.omp.mcastroutesrecv
==========================


Operation: GET /dataservice/device/omp/mcastroutesrecv
------------------------------------------------------


Get OMP multicast routes received list

.. code:: python

    def create_omp_mcast_routes_recv(device_id: str) -> List[Any]: ...


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
        client.device.omp.mcastroutesrecv.create_omp_mcast_routes_recv()


