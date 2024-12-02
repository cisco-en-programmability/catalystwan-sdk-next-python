===================================
device.omp.routes.received.omp_ipv6
===================================


Operation: GET /dataservice/device/omp/routes/received/ompIpv6
--------------------------------------------------------------


Get OMP received routes list (Real Time)

.. code:: python

    def create_received_routes_list_ipv6(device_id: str) -> List[Any]: ...


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
        client.device.omp.routes.received.omp_ipv6.create_received_routes_list_ipv6()


